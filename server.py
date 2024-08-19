from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()
class Student(BaseModel):
    name: str
    age: int

students = [
    {'name': 'Student 1', 'age': 20},
    {'name': 'Student 2', 'age': 18},
    {'name': 'Student 3', 'age': 16}
]

@app.get("/students")
def list_students():
    return students

@app.post('/students')
def user_add(student: Student):
    students.append(student)

    return {'student': students[-1]}