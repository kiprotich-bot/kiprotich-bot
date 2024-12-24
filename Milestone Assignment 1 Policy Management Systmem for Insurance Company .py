
class PolicyholderStatus(Enum):
    ACTIVE = "active"
    SUSPENDED = "suspended"
    TERMINATED = "terminated"

class Policyholder:
    def __init__(self, id: str, name: str, email: str, phone: str):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.status = PolicyholderStatus.ACTIVE
        self.policies = []
        self.registration_date = datetime.now()
        self.suspension_date = None
        
    def suspend(self, reason: str):
        self.status = PolicyholderStatus.SUSPENDED
        self.suspension_date = datetime.now()
        return f"Policyholder {self.id} suspended. Reason: {reason}"
        
    def reactivate(self):
        if self.status != PolicyholderStatus.TERMINATED:
            self.status = PolicyholderStatus.ACTIVE
            self.suspension_date = None
            return f"Policyholder {self.id} reactivated"
        return f"Cannot reactivate terminated policyholder {self.id}"
    
    def add_policy(self, policy):
        self.policies.append(policy)
        
    def get_account_details(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "status": self.status.value,
            "registration_date": self.registration_date,
            "policies": [{"id": p.id, "name": p.name, "premium": p.premium} for p in self.policies],
            "suspension_date": self.suspension_date
        }

class Product:
    def __init__(self, id: str, name: str, description: str, premium: float, coverage: dict):
        self.id = id
        self.name = name
        self.description = description
        self.premium = premium
        self.coverage = coverage
        self.is_active = True
        
    def update_premium(self, new_premium: float):
        self.premium = new_premium
        return f"Premium updated for product {self.id}"
        
    def update_coverage(self, new_coverage: dict):
        self.coverage = new_coverage
        return f"Coverage updated for product {self.id}"
        
    def suspend(self):
        self.is_active = False
        return f"Product {self.id} suspended"
        
    def reactivate(self):
        self.is_active = True
        return f"Product {self.id} reactivated"
        
    def get_details(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "premium": self.premium,
            "coverage": self.coverage,
            "is_active": self.is_active
        }

class PaymentStatus(Enum):
    PENDING = "pending"
    PAID = "paid"
    OVERDUE = "overdue"
    FAILED = "failed"

class Payment:
    def __init__(self, id: str, policyholder_id: str, product_id: str, amount: float, due_date: datetime):
        self.id = id
        self.policyholder_id = policyholder_id
        self.product_id = product_id
        self.amount = amount
        self.due_date = due_date
        self.payment_date = None
        self.status = PaymentStatus.PENDING
        self.penalties = 0
        
    def process_payment(self, payment_amount: float, payment_date: datetime):
        if payment_amount >= self.amount + self.penalties:
            self.payment_date = payment_date
            self.status = PaymentStatus.PAID
            return f"Payment {self.id} processed successfully"
        return f"Payment {self.id} failed - insufficient amount"
        
    def calculate_penalty(self, penalty_rate: float = 0.1):
        if self.status != PaymentStatus.PAID and datetime.now() > self.due_date:
            days_overdue = (datetime.now() - self.due_date).days
            self.penalties = self.amount * penalty_rate * days_overdue
            self.status = PaymentStatus.OVERDUE
            return self.penalties
        return 0
        
    def get_payment_details(self):
        return {
            "id": self.id,
            "policyholder_id": self.policyholder_id,
            "product_id": self.product_id,
            "amount": self.amount,
            "due_date": self.due_date,
            "payment_date": self.payment_date,
            "status": self.status.value,
            "penalties": self.penalties
        }
health_insurance = Product(
    "P001",
    "Comprehensive Health Insurance",
    "Full coverage health insurance with dental and vision",
    589.99,
    {"medical": 900000, "dental": 4000, "vision": 1000}
)

life_insurance = Product(
    "P002",
    "Term Life Insurance",
    "20-year term life insurance",
    299.99,
    {"death_benefit": 500000, "disability": 200000}
)

Jasmin = Policyholder("PH001", "Jasmin James", "jasmin@police.com", "444-0202")
Eliud = Policyholder("PH002", "Eliud Kipchoge", "Eliud@running.com", "444-0102")

jasmin.add_policy(health_insurance)
Eliud.add_policy(life_insurance)

payment1 = Payment(
    "PAY001",
    jasmin.id,
    health_insurance.id,
    health_insurance.premium,
    datetime.now() + timedelta(days=30)
)

payment2 = Payment(
    "PAY002",
    jasmin.id,
    life_insurance.id,
    life_insurance.premium,
    datetime.now() + timedelta(days=30)
)

payment1.process_payment(499.99, datetime.now())
payment2.process_payment(399.99, datetime.now())

print("Jasmin's Account Details:")
print(jasmin.get_account_details())
print("\nEliud's Account Details:")
print(Eliud.get_account_details())
