# FastAPI ToDo App

A simple ToDo application built with FastAPI, demonstrating CRUD operations (Create, Read, Update, Delete).

## Features

- **Create**: Add new tasks to the ToDo list.
- **Read**: Retrieve the list of all tasks and details of a specific task.
- **Update**: Modify the details of an existing task.
- **Delete**: Remove a task from the ToDo list.

## Installation
1.pip install fastapi <br>
2.pip install uvicorn



## Run the FastAPI application:
 1. uvicorn main:app --reload



API Endpoints
GET /todo: Retrieve all tasks.
GET /todo/{id}: Retrieve details of a specific task.
POST /todo: Add a new task.
PUT /todos/{id}: Update details of a task.
DELETE /todo/{id}: Delete a task.
