from fastapi import APIRouter, Query
from app.models import EmployeeCreate,EmployeeResponse, EmployeeUpdate
from app.services import employee_service
from app.utils.response import success_response

router = APIRouter(prefix="/employees", tags=["Employees"])

# CREATE
@router.post("/", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate):
    return employee_service.create_employee(employee)

# READ ALL + Query Param
@router.get("/")
def get_employees(min_age: int = Query(None)):
    employees = employee_service.get_all_employees()
    if min_age:
        employees = [e for e in employees if e["age"] >= min_age]
    return success_response(employees)

# READ ONE (Path Param)
@router.get("/{employee_id}")
def get_employee(employee_id: int):
    employee = employee_service.get_employee(employee_id)
    return success_response(employee)

    
'''
# UPDATE
@router.put("/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    updated_user = user_service.update_user(user_id, user)
    return success_response(updated_user, "User updated")

# DELETE
@router.delete("/{user_id}")
def delete_user(user_id: int):
    user_service.delete_user(user_id)
    return success_response(message="User deleted")
'''