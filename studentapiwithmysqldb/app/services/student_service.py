from sqlalchemy.orm import Session
from app.repositories.student_repository import StudentRepository
from app.utils.exceptions import StudentNotFoundException

class StudentService:

    @staticmethod
    def create_student(db: Session, student):
        return StudentRepository.create(db, student)

    @staticmethod
    def get_students(db: Session):
        return StudentRepository.get_all(db)

    @staticmethod
    def get_student(db: Session, student_id: int):
        student = StudentRepository.get_by_id(db,student_id)
        if not student:
            raise StudentNotFoundException("Student not found")
        return student

    @staticmethod
    def delete_student(db: Session, student_id: int):
        student = StudentRepository.delete(db, student_id)
        if not student:
            raise StudentNotFoundException("Student not found")
        return student