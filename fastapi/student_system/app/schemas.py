from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    age: int
    score: int


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    score: int

    class Config:
        orm_mode = True