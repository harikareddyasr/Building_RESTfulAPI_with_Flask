# Flask REST API Project

## Features:
- JWT Authentication
- Error Handling
- File Uploading
- Public & Admin Routes
- CRUD Operations

## Setup Instructions:

1. Create virtual environment:
    ```
    python -m venv venv
    ```

2. Activate environment:
    - Windows:
        ```
        venv\Scripts\activate
        ```
    - Mac/Linux:
        ```
        source venv/bin/activate
        ```

3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Create database:
    ```
    python
    >>> from run import app
    >>> from app import db
    >>> app.app_context().push()
    >>> db.create_all()
    >>> exit()
    ```

5. Run the app:
    ```
    python run.py
    ```

6. Test APIs using Postman.

## Team Members:
- Member 1
- Member 2
- Member 3
