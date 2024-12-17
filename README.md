
```python
import pandas as pd

# Replace 'salary_data.csv' with the path to your data file
salary_data = pd.read_csv('salary_data.csv')
print(salary_data.head())

```python
def get_employee_details(name):
    employee = salary_data[salary_data['Name'] == name]
    if not employee.empty:
        return employee.to_dict('records')[0]
    else:
        return "Employee not found."

# Example usage
print(get_employee_details('John Doe'))

salary_dict = salary_data.set_index('Name').to_dict('index')
print(salary_dict)
```

```python
def get_employee_details(name):
    try:
        employee = salary_data[salary_data['Name'] == name]
        if not employee.empty:
            return employee.to_dict('records')[0]
        else:
            return "Employee not found."
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
print(get_employee_details('John Doe'))
```
```python
import os
import zipfile

def export_employee_details(name):
    employee = get_employee_details(name)
    if isinstance(employee, dict):
        df = pd.DataFrame([employee])
        csv_filename = f"{name}_details.csv"
        df.to_csv(csv_filename, index=False)
        
        # Create a zip file
        with zipfile.ZipFile('Employee_Profile.zip', 'w') as zipf:
            zipf.write(csv_filename)
        
        # Clean up the CSV file
        os.remove(csv_filename)
        return "Employee details exported and zipped successfully."
    else:
        return employee

# Example usage
print(export_employee_details('John Doe'))
```

```r
# Unzip the folder
unzip("Employee_Profile.zip", ex dir = "Employee_Profile")

# Read the CSV file
employee_data <- read.csv("Employee_Profile/John_Doe_details.csv")
print(employee_data)
```

