from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

db = SQLAlchemy()


def gen_uuid():
    return str(uuid.uuid4())


class User(db.Model):
    __tablename__ = 'user'
    uuid = db.Column(db.String(36), primary_key=True, default=gen_uuid)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)


class Token(db.Model):
    __tablename__ = 'token'
    token = db.Column(db.String(36), primary_key=True)
    user_id = db.Column(db.String(36), db.ForeignKey('user.uuid'), nullable=False)
    exp_dt = db.Column(db.DateTime, nullable=False)


class Dream(db.Model):
    __tablename__ = 'dream'
    id = db.Column(db.String(36), primary_key=True, default=gen_uuid)
    user_id = db.Column(db.String(36), db.ForeignKey('user.uuid'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    upload_dt = db.Column(db.DateTime, default=datetime.utcnow)
