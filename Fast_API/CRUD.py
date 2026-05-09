from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Temporary storage
students = []

# Student Model
class Student(BaseModel):
    name: str
    age: int
    course: str
    marks: int


# 1️⃣ Create API – Add Student
@app.post("/students")
def add_student(student: Student):
    new_id = len(students) + 1

    new_student = {
        "id": new_id,
        "name": student.name,
        "age": student.age,
        "course": student.course,
        "marks": student.marks
    }

    students.append(new_student)

    return {"message": "Student added successfully"}


# 2️⃣ Create API – Get All Students
@app.get("/students")
def get_students():
    return students


# 3️⃣ Create API – Get Student By ID
@app.get("/students/{id}")
def get_student(id: int):
    for student in students:
        if student["id"] == id:
            return student

    raise HTTPException(status_code=404, detail="Student not found")


# 4️⃣ Create API – Update Student
@app.put("/students/{id}")
def update_student(id: int, updated_student: Student):
    for student in students:
        if student["id"] == id:
            student["name"] = updated_student.name
            student["age"] = updated_student.age
            student["course"] = updated_student.course
            student["marks"] = updated_student.marks

            return {"message": "Student updated successfully"}

    raise HTTPException(status_code=404, detail="Student not found")


# 5️⃣ Create API – Delete Student
@app.delete("/students/{id}")
def delete_student(id: int):
    for index, student in enumerate(students):
        if student["id"] == id:
            students.pop(index)
            return {"message": "Student deleted successfully"}

    raise HTTPException(status_code=404, detail="Student not found")
