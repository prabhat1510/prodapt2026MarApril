import os
from app.exceptions import StudentNotFoundException

students_db = []
student_id_counter = 1

CSV_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "students.csv")

def read_students_from_csv():
    global student_id_counter
    # Clear existing data to avoid duplicates on repeated calls
    students_db.clear()
    
    if not os.path.exists(CSV_FILE):
        return
    
    with open(CSV_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            student_data = line.split(", ")
            student_dict = {
                "id": int(student_data[0]),
                "name": student_data[1],
                "email": student_data[2],
                "age": int(student_data[3]),
                "grade": student_data[4]
            }
            students_db.append(student_dict)
            if int(student_data[0]) >= student_id_counter:
                student_id_counter = int(student_data[0]) + 1

def write_students_to_csv():
    with open(CSV_FILE, "w") as file:
        for student in students_db:
            file.write(f"{student['id']}, {student['name']}, {student['email']}, {student['age']}, {student['grade']}\n")

def get_student(id: int):
    read_students_from_csv()
    for student in students_db:
        if student["id"] == id:
            return student
    raise StudentNotFoundException(f"Student with id {id} not found")

def update_student(id: int, student_data):
    read_students_from_csv()
    for student in students_db:
        if student["id"] == id:
            student["name"] = student_data.name
            student["email"] = student_data.email
            student["age"] = student_data.age
            student["grade"] = student_data.grade
            write_students_to_csv()
            return student
    raise StudentNotFoundException(f"Student with id {id} not found")

def delete_student(id: int):
    read_students_from_csv()
    for student in students_db:
        if student["id"] == id:
            students_db.remove(student)
            write_students_to_csv()
            return student
    raise StudentNotFoundException(f"Student with id {id} not found")

def patch_student(id: int, student_data):
    read_students_from_csv()
    for student in students_db:
        if student["id"] == id:
            # Only update fields that were actually provided (not None)
            update_data = student_data.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                student[key] = value
            write_students_to_csv()
            return student
    raise StudentNotFoundException(f"Student with id {id} not found")