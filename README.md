# Dream Backend - README

## Overview

This is the backend service for the Dream Analysis application, built using Flask, SQLAlchemy, and MySQL. It provides RESTful APIs for user management and dream analysis functionalities.

---

## Prerequisites

Before setting up the backend, ensure you have the following installed:

1. **Python 3.8+**  
   [Download Python](https://www.python.org/downloads/)

2. **MySQL**  
   [Download MySQL](https://dev.mysql.com/downloads/)

3. **pip** (comes with Python)  
   Verify installation:  
   ```bash
   python --version
   pip --version
   ```

---

## Setup Instructions

### Step 1: Step into the Project Directory

```bash
cd dream-back
```

---

### Step 2: Create a Virtual Environment

Set up a Python virtual environment to isolate dependencies:

```bash
python -m venv venv
```

Activate the environment:

- **Linux/macOS**:
  ```bash
  source venv/bin/activate
  ```
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

---

### Step 3: Install Dependencies

Install the required Python packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### Step 4: Configure the Database

1. Start MySQL and create the database:
   ```sql
   CREATE DATABASE dreamdb CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
   ```

2. Update the `config.py` file with your database credentials:
   ```python
   DB_USER = 'your_mysql_user'
   DB_PASSWORD = 'your_mysql_password'
   DB_HOST = '127.0.0.1'
   DB_PORT = 3306
   DB_NAME = 'dream_db'
   ```

---

### Step 5: Initialize the Database

Run the following commands to initialize the database schema:

```bash
python
>>> from app import db
>>> db.create_all()
>>> exit()
```

---

--------------------------------------------------------------------------------------------------------------
对Step5做修正。
如果在运行Step5出现失败的情况，可能是因为SQLAlchemy版本太高导致。
通过一下方法来确认。
在venv环境中运行pip list命令，查看SQLAlchemy的版本，如果版本超过了3.0.0
那么Step5运行以下命令。注意DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME需要修改。


DB_USER = 'dreamdb'
DB_PASSWORD = 'Pass1234'

DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_NAME = 'dreamdb'

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"
SECRET_KEY = 'some-secret-key'


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)


with app.app_context():
    db.create_all()





-----------------------------------------------------------------------------------------------------------------




### Step 6: Start the Development Server

Run the backend service:

```bash
python app.py
```

The service will start at `http://127.0.0.1:5000`.

---

## API Endpoints

| Method | Endpoint               | Description                         |
|--------|-------------------------|-------------------------------------|
| POST   | `/api/user/register`   | Register a new user                |
| POST   | `/api/user/login`      | Login and get authentication token |
| GET    | `/api/analysis/list`   | Fetch the user's analysis history  |
| GET    | `/api/analysis/detail/<id>` | Fetch a specific analysis detail |
| POST   | `/api/analysis/new`    | Create a new dream analysis        |
| DELETE | `/api/analysis/delete/<id>` | Delete a specific analysis     |

---

## Development Notes

- **CORS**: This application uses `flask-cors` to handle cross-origin requests for front-end integration. Ensure the configuration matches your environment.
- **Token Authentication**: Users must log in to access analysis endpoints. Tokens are stored in the `token` table with an expiration date.
- **Environment Variables**: You can replace sensitive data like database credentials with environment variables for better security.

---

## Troubleshooting

### Common Issues
1. **Database Connection Error**  
   - Ensure MySQL is running and credentials in `config.py` are correct.
   - Test the connection manually:
     ```bash
     mysql -u your_mysql_user -p -h 127.0.0.1 -P 3306
     ```

2. **Package Installation Issues**  
   - Ensure you're in the virtual environment when running `pip install`.
   - Try upgrading `pip` if dependencies fail to install:
     ```bash
     pip install --upgrade pip
     ```

3. **Module Not Found**  
   - Check that `app.py` and `models.py` are in the same directory.
   - Verify `FLASK_APP` is correctly set if running via `flask run`.

