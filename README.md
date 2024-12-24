# Dream Backend - README

## Overview

This is the backend service for the Dream Analysis application, built using Flask, SQLAlchemy, and MySQL. It provides RESTful APIs for user management and dream analysis functionalities.

---

## Prerequisites


1. **Python 3.8+**  
   [Download Python](https://www.python.org/downloads/)

2. **MySQL 终端测试连接azure云端数据库是否成功** 
   *** 每次运行数据库应该都自动运行，但可以通过这个验证一下 ***
   ```bash
   mysql -u dreamdb -p -h 40.67.228.105 -P 3306 
   ``` 
   密码：Pass1234  

   ```sql:
   SHOW DATABASES;
   USE dreamdb;
   SHOW TABLES; 
   SELECT * FROM user;
   ``` 
   应该有数据库结构（USER等）,最后一行展示目前数据库存储的用户数据；

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
cd SSE-WEBPROJECT2
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

### Step 4: Start the Development Server

Run the backend service:

```bash
python app.py  
或者  
venv/bin/python app.py
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

