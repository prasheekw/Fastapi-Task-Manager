# FastAPI Task Manager API

A REST API for managing tasks, built while learning FastAPI and backend development.

The project started as a learning project while following a FastAPI course, and I implemented and tested the API while learning concepts such as database integration, authentication, CRUD operations, and API routing.

## Features

- User registration and login
- JWT-based authentication
- Password hashing
- Create, read, update, and delete tasks
- Request validation using Pydantic
- PostgreSQL database integration
- SQLAlchemy ORM
- Alembic database migrations
- API testing using Postman

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic
- JWT
- Postman

## Project Structure

├── migration/       
├── src/           
├── postman/         
├── app.py           
├── alembic.ini      
├── .gitignore
└── README.md

## Running the Project

1. Clone the repository
    git clone <your-github-repository-url>
    cd <project-folder>

2. Create and activate a virtual environment
    python -m venv env

Windows command to activate env:
    env\Scripts\activate

3. Install dependencies
    pip install -r requirements.txt

4. Configure environment variables
    Create a .env file and add the required database and authentication configuration.

Example:

DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key

5. Run database migrations
    alembic upgrade head

6. Start the FastAPI server
    uvicorn app:app --reload

The API will be available at:

    http://127.0.0.1:8000

FastAPI's interactive API documentation is available at:

    http://127.0.0.1:8000/docs

## API Testing

A Postman collection is included in the postman/ directory.

The collection can be imported into Postman to test the API endpoints.

The API was manually tested during development using Postman, including authentication and task CRUD operations.

## What I Learned

Through this project, I practiced:

Building REST APIs with FastAPI
Working with HTTP methods and API routes
Structuring a FastAPI application
Connecting an API to a PostgreSQL database
Using SQLAlchemy for database operations
Creating and managing database migrations with Alembic
Implementing JWT authentication
Hashing user passwords
Handling user-specific resources
Validating API requests with Pydantic
Testing API endpoints with Postman
Current Status

This project represents my practical work while learning FastAPI and backend development.

Automated testing, Docker containerization, and cloud deployment are not currently implemented.