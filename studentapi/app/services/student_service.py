from app.database import students_db, student_id_counter
from app.exceptions import StudentNotFoundException

 #create a new student and assign an ID
def create_student(student_data):
    
    #Accessing global variables
    global student_id_counter
   
    #Creating a dictionay from student_data model
    student = student_data.dict()
    #Adding new key:value to the dictionary
    student["id"] = student_id_counter
    #Adding the student dictionary to list of students_db
    students_db.append(student)
    #Incrementing student id counter
    student_id_counter += 1
    #returning the student model or object to the calling function
    return student

def get_all_students():
    return students_db