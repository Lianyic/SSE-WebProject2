import os

from flask import Flask, request, jsonify, make_response, send_from_directory, abort
from models import db, User, Token, Dream
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import uuid
from flask_cors import CORS

import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = config.SECRET_KEY

db.init_app(app)
with app.app_context():
    db.create_all()

CORS(app, supports_credentials=True)


def get_current_user():
    token = request.cookies.get('token')
    if not token:
        return None
    tk = Token.query.filter_by(token=token).first()
    if tk and tk.exp_dt > datetime.utcnow():
        return User.query.filter_by(uuid=tk.user_id).first()
    return None


@app.route('/api/user/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "User exists"}), 400

    hashed = generate_password_hash(password)
    u = User(username=username, password=hashed)
    db.session.add(u)
    db.session.commit()
    return jsonify({"msg": "Registered"}), 200


@app.route('/api/user/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"error": "Invalid credentials"}), 401

    # create token
    t = str(uuid.uuid4())
    exp = datetime.utcnow() + timedelta(days=1)
    tk = Token(token=t, user_id=user.uuid, exp_dt=exp)
    db.session.add(tk)
    db.session.commit()

    resp = make_response(jsonify({"msg": "Login success"}), 200)
    resp.set_cookie('token', t, httponly=True, samesite='None', secure=True)
    return resp


@app.route('/api/analysis/list', methods=['GET'])
def analysis_list():
    user = get_current_user()
    if not user:
        return jsonify({"error": "Not authorized"}), 401

    items = Dream.query.filter_by(user_id=user.uuid).all()

    data = []
    for i in items:
        data.append({
            "id": i.id,
            "query": i.content,
            "answer": i.answer,
            "upload_dt": i.upload_dt.strftime('%Y-%m-%d %H:%M:%S')
        })
    return jsonify(data), 200


@app.route('/api/analysis/detail/<id>', methods=['GET'])
def analysis_detail(id):
    user = get_current_user()
    if not user:
        return jsonify({"error": "Not authorized"}), 401
    item = Dream.query.filter_by(id=id, user_id=user.uuid).first()
    if not item:
        return jsonify({"error": "Not found"}), 404
    return jsonify({
        "id": item.id,
        "query": item.content,
        "answer": item.answer,
        "upload_dt": item.upload_dt.strftime('%Y-%m-%d %H:%M:%S')
    }), 200


@app.route('/api/analysis/new', methods=['POST'])
def analysis_new():
    user = get_current_user()
    if not user:
        return jsonify({"error": "Not authorized"}), 401
    data = request.json
    query = data.get('query')
    # do some analysis
    answer = "Your dream means something nice..."
    a = Dream(user_id=user.uuid, content=query, answer=answer)
    db.session.add(a)
    db.session.commit()
    return jsonify({"msg": "Created"}), 200


@app.route('/api/analysis/delete/<id>', methods=['DELETE'])
def analysis_delete(id):
    user = get_current_user()
    if not user:
        return jsonify({"error": "Not authorized"}), 401
    item = Dream.query.filter_by(id=id, user_id=user.uuid).first()
    if not item:
        return jsonify({"error": "Not found"}), 404
    db.session.delete(item)
    db.session.commit()
    return jsonify({"msg": "Deleted"}), 200


@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')


@app.route('/<path:subpath>')
def serve_page(subpath):
    static_dir = os.path.join(app.root_path, 'templates')

    filepath = os.path.join(static_dir, subpath)

    if not os.path.commonpath([static_dir, os.path.abspath(filepath)]).startswith(static_dir):
        return send_from_directory('templates', '404.html'), 404
    if ".txt" in subpath:
        if os.path.exists(filepath) and os.path.isfile(filepath):
            return send_from_directory(static_dir, subpath)
        else:
            return send_from_directory('templates', '404.html'), 404

    return send_from_directory(static_dir, f"{subpath}.html")


@app.route('/_next/static/<path:subpath>')
def serve_static(subpath):
    static_dir = os.path.join(app.root_path, 'static')
    filepath = os.path.join(static_dir, subpath)

    if not os.path.commonpath([static_dir, os.path.abspath(filepath)]).startswith(static_dir):
        abort(404)

    if os.path.exists(filepath) and os.path.isfile(filepath):
        return send_from_directory(static_dir, subpath)

    abort(404)


if __name__ == '__main__':
    app.run(debug=True)
