from fastapi import APIRouter, Query
from app.models import Student,StudentResponse
from app.services import student_service
from app.utils.response import success_response

# Creating a router for student routes with prefix and tag
# This will prefix all routes with /students
router = APIRouter(prefix="/students", tags=["Students"])

# CREATE
# POST /students/add
# This will create a new student and return the created student
# The response_model parameter is used to specify the response model
@router.post("/add", response_model=StudentResponse)
def create_student(student: Student):
    # Calling the service function to create a student
    return student_service.create_student(student)

# READ ALL 
# GET /students/all
# This will return all students
@router.get("/all")
def get_students():
    # Calling the service function to get all students
    students = student_service.get_all_students()
    # Returning a success response with the students data
    return success_response(students)