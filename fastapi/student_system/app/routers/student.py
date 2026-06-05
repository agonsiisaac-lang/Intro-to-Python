from fastapi import APIRouter
from app.schemas import StudentCreate
from app.crud import (
    create_student,
    get_students,
    get_student,
    delete_student
)

router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/")
def add_student(student: StudentCreate):

    return create_student(student)


@router.get("/")
def read_students():

    return get_students()

@router.get("/{student_id}")
def read_student(student_id: int):

    return get_student(student_id)

@router.delete("/{student_id}")
def remove_student(student_id: int):

    return delete_student(student_id)

