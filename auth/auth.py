from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
import datetime

auth_blueprint = Blueprint("auth", __name__)

@auth_blueprint.route('/login', methods=['POST'])
def login():
    username = request.json.get("admin")
    password = request.json.get("cpe1234")
    if username == "admin" and password == "password":  # simple authentication example
        access_token = create_access_token(identity=username, expires_delta=datetime.timedelta(days=1))
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Invalid credentials"}), 401
