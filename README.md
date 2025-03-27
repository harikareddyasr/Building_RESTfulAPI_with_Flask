
# Flask REST API Project

## Features

- JWT Authentication  
- Error Handling  
- File Uploading  
- Public & Admin Routes  
- CRUD Operations  

---

## Folder Structure

```
flask_rest_api_project/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── public_routes.py
│   │   └── admin_routes.py
│   └── utils/
│       ├── __init__.py
│       └── error_handlers.py
│
├── uploads/
├── instance/
├── .env
├── .gitignore
├── requirements.txt
├── run.py
└── README.md
```

---

## Setup Instructions

1. Clone or Download the Repository  
   ```
   git clone https://github.com/yourusername/flask_rest_api_project.git
   cd flask_rest_api_project
   ```

2. Create Virtual Environment  
   ```
   python -m venv venv
   ```

3. Activate the Environment  
   - Windows:  
     ```
     venv\Scripts\activate
     ```
   - Mac/Linux:  
     ```
     source venv/bin/activate
     ```

4. Install Dependencies  
   ```
   pip install -r requirements.txt
   ```

5. Set Up Environment Variables  
   Create a `.env` file in the project root and add:  
   ```
   DATABASE_URI = sqlite:///site.db
   _SECRET_KEY = supersecretkey
   ```

6. Create the Database  
   ```
   python
   >>> from run import app
   >>> from app import db
   >>> app.app_context().push()
   >>> db.create_all()
   >>> exit()
   ```

7. Run the App  
   ```
   python run.py
   ```
   The app will run at: http://127.0.0.1:5000

---

## API Endpoints

### Public Routes

- `GET /items` – Get all public items

### Admin Routes (Authentication Required)

- `POST /admin/register` – Register new user  
- `POST /admin/login` – Login & get JWT token  
- `GET /admin/dashboard` – Test protected route  
- `POST /admin/item` – Create new item  
- `PUT /admin/item/<id>` – Update an item  
- `DELETE /admin/item/<id>` – Delete an item  
- `POST /admin/upload` – Upload a file

---

## File Upload Notes

- Allowed Types: `.png`, `.jpg`, `.jpeg`, `.pdf`  
- Max File Size: 2 MB  
- Uploads saved in: `/uploads` directory

---

## Team Members

- Snigdha Aravapalli  
  Email: snigdha.aravapalli@csu.fullerton.edu  

- Harika Animireddy Gari  
  Email: Harikareddy@csu.fullerton.edu  

- Yashwanth Reddy Mallareddygari  
  Email: YashwanthR@csu.fullerton.edu

