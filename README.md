# Task Management API

A secure backend REST API built with FastAPI for managing user-based tasks.
The application implements JWT authentication, ownership validation, and structured service-based architecture.

This project demonstrates backend engineering fundamentals including authentication flows, relational database modeling, and clean separation of concerns.


## Tech Stack

- Python 3.12
- FastAPI
- SQLAlchemy (ORM)
- MariaDB
- JWT Authentication
- Pydantic
- Uvicorn


## Features

- User registration
- Secure login with JWT authentication
- Protected routes
- Task CRUD operations
- Task ownership validation (users can only access their own tasks)
- Enum-based status validation (todo / in_progress / done)
- Environment-based configuration


## API Endpoints

### Authentication
- POST /register - Create a new user 
- POST /login - Authenticate and receive JWT token

### Tasks
- GET /tasks - Retrieve authenticated user's tasks
- POST /tasks - Create a new task
- PUT /tasks/{id}/update - Update task (ownership potected)
- DELETE /tasks/{id} - Delete task (ownership protected)


## How to Run Locally

1. git clone <repository-url>
2. cd Task-Management-API
3. python -m venv .venv
4. source .venv/bin/activate  # Windows: .venv\Scripts\activate
5. pip install -r requirements.txt
6. uvicorn app.main:app --reload
   
Swagger documentation available at:
- http://127.0.0.1:8000/docs


## Project Architecture
The project follows a layered structure:

- Routes -> HTTP layer
- Services -> Business logic
- Models -> Database structure
- Schemas -> Data validation
- Auth -> JWT handling

This separation ensures maintainability and scalability.

## Future Improvements

- Pagination support
- Automated testing with Pytest
- Docker containerization
- CI/CD integration
