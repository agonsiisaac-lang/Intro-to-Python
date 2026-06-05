from app.models import Student
from app.database import SessionLocal

db = SessionLocal()

def create_student(student):

    new_student = Student(
        name=student.name,
        age=student.age,
        score=student.score
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student

def get_students():

    return db.query(Student).all()


def get_student(student_id: int):

    return db.query(Student).filter(
        Student.id == student_id
    ).first()

def delete_student(student_id: int):

    student = get_student(student_id)

    if student:
        db.delete(student)
        db.commit()

    return student

