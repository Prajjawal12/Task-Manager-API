# Task Manager API

This is a Django-based API for managing tasks. It utilizes MySQL as the database and Django REST framework for creating the API endpoints.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)

## Prerequisites

Before setting up the project, ensure you have the following installed on your system:

- [Anaconda](https://www.anaconda.com/products/distribution#download-section) (for managing Python environments)
- [MySQL Server](https://dev.mysql.com/downloads/mysql/) (to host the database)
- [Python 3.x](https://www.python.org/downloads/) (ensure it's compatible with your Django version)

## Setup Instructions

Follow these steps to set up the project:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Prajjawal12/Task-Manager-API.git
   cd Task-Manager-API
   ```

2. **Create a Conda Environment**

   Create a new Conda environment for your project:

   ```bash
   conda create --name task_manager python=3.10
   conda activate task_manager
   ```

3. **Install Required Packages**

   ```bash
   pip install django djangorestframework pymysql mysqlclient
   ```

4. **Configure MySQL Database**

   - Start your MySQL server
   - Open your MySQL client
   - Create a new database:
     ```sql
     CREATE DATABASE your_database_name;
     ```

5. **Update settings.py**

   Ensure your database configurations match your MySQL setup:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_database_name',
           'USER': 'username',  # your MySQL username
           'PASSWORD': 'password',  # your MySQL password
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

6. **Run Migrations**

   ```bash
   python manage.py migrate
   ```

## Running the Project

1. **Start the Development Server**

   ```bash
   python manage.py runserver
   ```

2. **Access the API**

   Once the server is running, access the API at http://127.0.0.1:8000/

   # Task Manager Project Structure

```
task_manager/
├── manage.py
├── task_manager/
│   ├── __pycache__/
│   │   ├── __init__.py
│   │   └── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── tasks/
    ├── __pycache__/
    ├── migrations/
    ├── models/
    │   ├── __pycache__/
    │   ├── enums/
    │   │   ├── __init__.py
    │   │   ├── task.py
    │   │   └── user.py
    │   └── serializers/
    │       ├── __pycache__/
    │       ├── task_serializer.py
    │       └── user_serializer.py
    └── views/
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── tests.py
        ├── urls.py
        └── views.py
```

# Task Manager API Documentation

## Base URL

All endpoints are prefixed with the base URL:

```
http://127.0.0.1:8000/api/
```

## Endpoints

### 1. Get Users for a Specific Task

- **Endpoint:** `/tasks/<task_id>/users/`
- **Method:** GET
- **Description:** Retrieve a list of users assigned to a specific task.

**Request Example:**

```http
GET /api/tasks/1/users/
```

**Sample Response:**

```json
{
  "users": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com",
      "mobile": "1234567890"
    },
    {
      "id": 2,
      "name": "Jane Smith",
      "email": "jane.smith@example.com",
      "mobile": "0987654321"
    }
  ]
}
```

### 2. Create a User

- **Endpoint:** `/users/`
- **Method:** `POST`
- **Description:** Create a new user.

**Request Example:**

```http
POST /api/users/
Content-Type: application/json

{
    "name": "Alice Johnson",
    "email": "alice.johnson@example.com",
    "mobile": "1231231234"
}
```

**Sample Response:**

```json
{
  "id": 3,
  "name": "Alice Johnson",
  "email": "alice.johnson@example.com",
  "mobile": "1231231234",
  "created_at": "2024-10-22T12:34:56Z"
}
```

### 3. Get Tasks for a Specific User

- **Endpoint:** `/users/<user_id>/tasks/`
- **Method:** `GET`
- **Description:** Retrieve a list of tasks assigned to a specific user.

**Request Example:**

```http
GET /api/users/1/tasks/
```

**Sample Response:**

```json
{
  "tasks": [
    {
      "id": 1,
      "name": "Task 1",
      "description": "Description for Task 1",
      "created_at": "2024-10-21T12:00:00Z",
      "updated_at": "2024-10-22T12:00:00Z",
      "status": "pending",
      "task_type": "work"
    },
    {
      "id": 2,
      "name": "Task 2",
      "description": "Description for Task 2",
      "created_at": "2024-10-20T10:00:00Z",
      "updated_at": "2024-10-21T11:00:00Z",
      "status": "completed",
      "task_type": "personal"
    }
  ]
}
```

### 4. Assign User to Task

- **Endpoint:** `/tasks/assign/`
- **Method:** `POST`
- **Description:** Assign one or more users to a specific task.

**Request Example:**

```http
POST /api/tasks/assign/
Content-Type: application/json

{
    "user_ids": [1, 2],
    "task_id": 1
}
```

**Sample Response:**

```json
{
  "message": "Users assigned to task successfully."
}
```

### 5. Create a Task

- **Endpoint:** `/tasks/`
- **Method:** `POST`
- **Description:** Create a new task.

**Request Example:**

```http
POST /api/tasks/
Content-Type: application/json

{
    "name": "New Task",
    "description": "This is a new task.",
    "task_type": "work"
}
```

**Sample Response:**

```json
{
  "id": 3,
  "name": "New Task",
  "description": "This is a new task.",
  "created_at": "2024-10-22T12:34:56Z",
  "updated_at": "2024-10-22T12:34:56Z",
  "status": "pending",
  "task_type": "work"
}
```

## Error Handling

If a request fails (e.g., due to validation errors), the API will respond with a relevant error message. Here is an example of an error response:

**Sample Error Response:**

```json
{
  "error": "One or more users do not exist."
}
```
