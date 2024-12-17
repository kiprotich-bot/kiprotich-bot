
import pandas as pd

salary_data = pd.read_csv('salary_data.csv')
print(salary_data.head())

def get_employee_details(name):
    employee = salary_data[salary_data['Name'] == name]
    if not employee.empty:
        return employee.to_dict('records')[0]
    else:
        return "Employee not found."

salary_dict = salary_data.set_index('Name').to_dict('index')
print(salary_dict)
```

def export_employee_details(name):
    employee = get_employee_details(name)
    if is instance(employee, dict):
        df = pd.DataFrame([employee])
        csv_filename = f"{name}_details.csv"
        df.to_csv(csv_filename, index=False)
        
        with zipfile.ZipFile('Employee_Profile.zip', 'w') as Zipf:
            Zipf.write(csv_filename)
        
        os.remove(csv_filename)
        return "Employee details exported and zipped successfully."
    else:
        return employee


R Script to unzip and display data\n",
    "\n",
    "```R\n",
    "# R Script for unzipping and displaying employee profile\n",
    "library(utils)\n",
    "\n",
    "# Unzip the file\n",
    "unzip(\"Employee Profile.zip\", ex dir = \"Employee Profile\")\n",
    "\n",
    "# Read and display the CSV\n",
    "employee_data <- read.csv(\"Employee Profile/John_Doe_profile.csv\")\n",
    "print(employee_data)\n",
    "```"
