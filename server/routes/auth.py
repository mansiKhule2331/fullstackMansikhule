from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models.db import get_db
import bcrypt
from datetime import datetime

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json() or {}
    name = data.get("name", "").strip()
    email = data.get("email", "").strip().lower()
    password = data.get("password", "")
    role = data.get("role", "user")

    if not name or not email or not password:
        return jsonify({"error": "name, email and password are required"}), 400

    db = get_db()
    if db.users.find_one({"email": email}):
        return jsonify({"error": "Email already registered"}), 409

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    user_doc = {
        "name": name,
        "email": email,
        "password": hashed,
        "role": role if role in ("user", "admin") else "user",
        "last_login": None,
        "login_count": 0,
        "created_at": datetime.utcnow(),
    }
    result = db.users.insert_one(user_doc)
    return jsonify({"message": "Registered successfully", "id": str(result.inserted_id)}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    email = data.get("email", "").strip().lower()
    password = data.get("password", "")

    if not email or not password:
        return jsonify({"error": "email and password are required"}), 400

    db = get_db()
    user = db.users.find_one({"email": email})
    if not user or not bcrypt.checkpw(password.encode(), user["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    # Update login stats
    db.users.update_one(
        {"email": email},
        {"$set": {"last_login": datetime.utcnow()}, "$inc": {"login_count": 1}},
    )

    token = create_access_token(identity=str(user["_id"]))
    return jsonify({
        "access_token": token,
        "user": {
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"],
            "role": user.get("role", "user"),
        },
    }), 200
