
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
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Employee Salary Data Analysis\n",
    "\n",
    "## Assignment Tasks\n",
    "1. Import Data\n",
    "2. Create Employee Function\n",
    "3. Data Processing with Dictionary\n",
    "4. Error Handling\n",
    "5. Export Employee Details\n",
    "6. Unzip and Display Data with R"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "import pandas as pd\n",
    "import os\n",
    "import csv\n",
    "import zipfile"
   ],
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 1: Import Data\n",
    "We'll simulate importing salary data by creating a sample DataFrame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "# Sample salary data\n",
    "salary_data = pd.DataFrame([\n",
    "    {\"Name\": \"John Doe\", \"Department\": \"HR\", \"Salary\": 75000, \"Years of Experience\": 5},\n",
    "    {\"Name\": \"Jane Smith\", \"Department\": \"IT\", \"Salary\": 85000, \"Years of Experience\": 7},\n",
    "    {\"Name\": \"Mike Johnson\", \"Department\": \"Finance\", \"Salary\": 90000, \"Years of Experience\": 10},\n",
    "    {\"Name\": \"Sarah Williams\", \"Department\": \"Marketing\", \"Salary\": 70000, \"Years of Experience\": 4}\n",
    "])\n",
    "\n",
    "print(salary_data)"
   ],
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2: Create Employee Function\n",
    "Develop a function to retrieve employee details"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "def get_employee_details(name):\n",
    "    \"\"\"\n",
    "    Retrieve employee details by name\n",
    "    \n",
    "    Args:\n",
    "        name (str): Name of the employee\n",
    "    \n",
    "    Returns:\n",
    "        dict: Employee details\n",
    "    \"\"\"\n",
    "    try:\n",
    "        # Find employee by name\n",
    "        employee = salary_data[salary_data['Name'] == name]\n",
    "        \n",
    "        if employee.empty:\n",
    "            raise ValueError(f\"No employee found with name: {name}\")\n",
    "        \n",
    "        return employee.to_dict('records')[0]\n",
    "    except Exception as e:\n",
    "        print(f\"Error retrieving employee details: {e}\")\n",
    "        return None\n",
    "\n",
    "# Test the function\n",
    "print(get_employee_details(\"John Doe\"))"
   ],
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 3: Data Processing with Dictionary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "# Create a dictionary of employees\n",
    "employees_dict = {row['Name']: row for _, row in salary_data.iterrows()}\n",
    "\n",
    "# Process and analyze data\n",
    "def analyze_department_salaries():\n",
    "    department_salaries = {}\n",
    "    for employee in employees_dict.values():\n",
    "        dept = employee['Department']\n",
    "        salary = employee['Salary']\n",
    "        \n",
    "        if dept not in department_salaries:\n",
    "            department_salaries[dept] = {'total_salary': 0, 'count': 0}\n",
    "        \n",
    "        department_salaries[dept]['total_salary'] += salary\n",
    "        department_salaries[dept]['count'] += 1\n",
    "    \n",
    "    # Calculate average salaries\n",
    "    for dept, data in department_salaries.items():\n",
    "        data['avg_salary'] = data['total_salary'] / data['count']\n",
    "    \n",
    "    return department_salaries\n",
    "\n",
    "print(analyze_department_salaries())"
   ],
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4: Error Handling\n",
    "We've already implemented error handling in the previous functions"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 5: Export Employee Details"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "def export_employee_profile(name):\n",
    "    \"\"\"\n",
    "    Export employee details to a CSV file and zip it\n",
    "    \n",
    "    Args:\n",
    "        name (str): Name of the employee\n",
    "    \"\"\"\n",
    "    try:\n",
    "        # Get employee details\n",
    "        employee = get_employee_details(name)\n",
    "        \n",
    "        if not employee:\n",
    "            raise ValueError(\"Could not retrieve employee details\")\n",
    "        \n",
    "        # Create directory if it doesn't exist\n",
    "        os.makedirs(\"Employee Profile\", exist_ok=True)\n",
    "        \n",
    "        # Export to CSV\n",
    "        csv_filename = f\"Employee Profile/{name.replace(' ', '_')}_profile.csv\"\n",
    "        with open(csv_filename, 'w', newline='') as csvfile:\n",
    "            writer = csv.DictWriter(csvfile, fieldnames=employee.keys())\n",
    "            writer.writeheader()\n",
    "            writer.writerow(employee)\n",
    "        \n",
    "        # Zip the file\n",
    "        with zipfile.ZipFile(\"Employee Profile.zip\", 'w') as zipf:\n",
    "            zipf.write(csv_filename, os.path.basename(csv_filename))\n",
    "        \n",
    "        print(f\"Profile for {name} exported successfully\")\n",
    "    except Exception as e:\n",
    "        print(f\"Error exporting employee profile: {e}\")\n",
    "\n",
    "# Export John Doe's profile\n",
    "export_employee_profile(\"John Doe\")"
   ],
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 6: Unzip and Display Data with R\n",
    "R Script to unzip and display data\n",
    "\n",
    "```R\n",
    "# R Script for unzipping and displaying employee profile\n",
    "library(utils)\n",
    "\n",
    "# Unzip the file\n",
    "unzip(\"Employee Profile.zip\", exdir = \"Employee Profile\")\n",
    "\n",
    "# Read and display the CSV\n",
    "employee_data <- read.csv(\"Employee Profile/John_Doe_profile.csv\")\n",
    "print(employee_data)\n",
    "```"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

