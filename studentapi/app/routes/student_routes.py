from fastapi import APIRouter, Query
from app.models import Student,StudentResponse
from app.services import student_service
from app.utils.response import success_response
from app.utils.loggers import logger
# Creating a router for student routes with prefix and tag
# This will prefix all routes with /students
router = APIRouter(prefix="/students", tags=["Students"])

# CREATE
# POST /students/add
# This will create a new student and return the created student
# The response_model parameter is used to specify the response model
@router.post("/add", response_model=StudentResponse)
def create_student(student: Student):
    logger.info("Inside employee routes")
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


# READ BY ID
# GET /students/{id}
# This will return the student with the given id
@router.get("/{id}")
def get_student(id: int):
    # Calling the service function to get the student
    student = student_service.get_student(id)
    # Returning a success response with the students data
    return success_response(student)


# UPDATE
# PUT /students/{id}
# This will update the student with the given id
@router.put("/{id}")
def update_student(id: int, student: Student):
    # Calling the service function to update the student
    student = student_service.update_student(id, student)
    # Returning a success response with the students data
    return success_response(student)


# DELETE
# DELETE /students/{id}
# This will delete the student with the given id
@router.delete("/{id}")
def delete_student(id: int):
    # Calling the service function to delete the student
    student = student_service.delete_student(id)
    # Returning a success response with the students data
    return success_response(student)


