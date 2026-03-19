from sqlalchemy.orm import Session
from app.models.student_model import Student

class StudentRepository:

    @staticmethod
    def create(db: Session, student):
        db_student = Student(name=student.name, email=student.email)
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student

    @staticmethod
    def get_all(db: Session):
        return db.query(Student).all()

    @staticmethod
    def get_by_id(db: Session, student_id: int):
        return db.query(Student).filter(Student.id == student_id).first()

    @staticmethod
    def delete(db: Session, student_id: int):
        student = db.query(Student).filter(Studentser.id == student_id).first()
        if student:
            db.delete(student)
            db.commit()
        return user