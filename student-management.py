from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class student(BaseModel):
    Name:str
    SIC:str
    Roll_No:int

students: List[student] = []

# @app.get("/")
# def read_root():
#     return {"Message":"Student's name has been added to the database.."}



@app.post("/students")
def add_student(new_student:student):
    students.append(new_student)
    return new_student

@app.get("/students")
def get_student():
    return students


@app.put("/students/update/{student_name}")
def print_studentName(student_name:str,updated_List:student):
    for i,student in enumerate(students):
        if student.Name == student_name:
            students[i] = updated_List
            return updated_List
    
    return {"Message":"No match found.."}

@app.delete("/students/delete/{student_SIC}")
def delete_student(student_SIC:str):
    for i,student in enumerate(students):
        if student.SIC == student_SIC:
            students.pop(i)
            return {"MEssage":"Student deleted successfully"}
             
        
    return {"Message":"No match found.."}

@app.get("/students/{roll_no}")
def show_roll_no(roll_no:int):
    for i,student in enumerate(students):
        if student.Roll_No == roll_no:
            return student
    
    return {"Message":"No match found.."}