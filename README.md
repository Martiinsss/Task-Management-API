# Task Management API

A production-ready RESTful API for managing tasks, built using FastAPI and MariaDB.  
This project demonstrates backend best practices including JWT authentication, relational database modeling, Docker containerization, and clean architecture principles.

The API supports user registration, authentication, and full CRUD operations for task management, with secure access control and structured error handling.


## Tech Stack

- Python
- FastAPI
- MariaDB
- SQLAlchemy
- JWT Authentication
- Docker
- Pytest


## Features

- User registration and authentication (JWT)
- Secure password hashing
- CRUD operations for tasks
- Task filtering and pagination
- Role-based access control
- Structured error handling
- Dockerized deployment


## API Endpoints

### Auth
- POST /register
- POST /login

### Tasks
- GET /tasks
- POST /tasks
- PUT /tasks/{id}
- DELETE /tasks/{id}


## How to Run

1. Clone the repository
2. Create a virtual environment
3. Install dependencies:
   pip install -r requirements.txt
4. Run the application:
   uvicorn app.main:app --reload
