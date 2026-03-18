from app.database import employees_db, employee_id_counter
from app.exceptions import EmployeeNotFoundException

def create_employee(employee_data):
    global employee_id_counter
    employee = employee_data.dict()
    employee["id"] = employee_id_counter
    employees_db.append(employee)
    employee_id_counter += 1
    return employee

def get_all_employees():
    return employees_db

def get_employee(employee_id: int):
    for employee in employees_db:
        if employee["id"] == employee_id:
            return employee
    raise EmployeeNotFoundException("employee not found")

def update_employee(employee_id: int, update_data):
    for employee in employees_db:
        if employee["id"] == employee_id:
            for key, value in update_data.dict(exclude_unset=True).items():
                employee[key] = value
            return employee
    raise EmployeeNotFoundException("employee not found")

def delete_employee(employee_id: int):
    for employee in employees_db:
        if employee["id"] == employee_id:
            employees_db.remove(employee)
            return
    raise EmployeeNotFoundException("Employee not found")
