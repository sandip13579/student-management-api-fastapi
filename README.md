 Student Management API - Version 1

A simple Student Management API built using FastAPI and Pydantic. This is Version 1 of the project, where student data is stored temporarily in memory using Python lists and CRUD operations are implemented.

 Features

* Add Student
* Get All Students
* Get Student by Roll Number
* Update Student Details
* Delete Student Records
* Request Validation using Pydantic
* Interactive API Documentation with Swagger UI

 Technologies Used

* Python
* FastAPI
* Pydantic

 API Endpoints

 Create Student

POST /students

 Get All Students

GET /students

 Get Student by Roll Number

GET /students/{roll_no}

 Update Student Details

PUT /students/update/{student_name}

 Delete Student

DELETE /students/delete/{student_SIC}

 Project Status

Version 1 ✅

Current implementation stores data in memory using Python lists. Data is lost when the server restarts.

 Planned Improvements (Version 2)

* SQLite Database Integration
* Persistent Data Storage
* Better Error Handling
* Modular Project Structure

 Run Locally

1. Clone the repository

2. Install dependencies

pip install -r requirements.txt

3. Start the server

uvicorn main:app --reload

4. Open Swagger UI

http://127.0.0.1:8000/docs#/

