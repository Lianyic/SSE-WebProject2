import os

##DB_USER = 'root'
##DB_PASSWORD = '15923516067Ll!'


DB_USER = 'dreamdb'
DB_PASSWORD = 'Pass1234'

DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_NAME = 'dreamdb'

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"
SECRET_KEY = 'some-secret-key'
