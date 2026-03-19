import app.database as db
from app.exceptions import StudentNotFoundException
from app.utils.loggers import logger
from app.models import Student, StudentUpdate

# create a new student and assign an ID
def create_student(student_data):

    # Creating a dictionary from student_data model
    student = student_data.dict()
    # Adding new key:value to the dictionary
    student["id"] = db.student_id_counter
    # Adding the student dictionary to list of students_db
    db.students_db.append(student)
    # Incrementing student id counter
    db.student_id_counter += 1

    # Write updated data to CSV
    db.write_students_to_csv()
    logger.info(f"Student data created successfully with id: {student['id']}")
    # returning the student model or object to the calling function
    return student

def get_all_students():
    db.read_students_from_csv()
    return db.students_db


# READ BY ID
# GET /students/{id}
# This will return the student with the given id
def get_student(id: int):
    # Calling the database function to get the student
    student = db.get_student(id)
    logger.info(f"Student data retrieved successfully with id: {id}")
    # Returning the student model or object to the calling function
    return student


# UPDATE
# PUT /students/{id}
# This will update the student with the given id
def update_student(id: int, student_data: Student):
    # Calling the database function to update the student
    student = db.update_student(id, student_data)
    logger.info(f"Student data updated successfully with id: {id}")
    # Returning the student model or object to the calling function
    return student


# DELETE
# DELETE /students/{id}
# This will delete the student with the given id
def delete_student(id: int):
    # Calling the database function to delete the student
    student = db.delete_student(id)
    logger.info(f"Student data deleted successfully with id: {id}")
    # Returning the student model or object to the calling function
    return student

# PATCH
# PATCH /students/{id}
# This will partially update the student with the given id
def patch_student(id: int, student_data: StudentUpdate):
    # Calling the database function to patch the student
    student = db.patch_student(id, student_data)
    logger.info(f"Student data patched successfully with id: {id}")
    # Returning the student model or object to the calling function
    return student
