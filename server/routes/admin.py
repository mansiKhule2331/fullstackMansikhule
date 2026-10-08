from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.db import get_db
from bson import ObjectId
from datetime import datetime
from functools import wraps

admin_bp = Blueprint("admin", __name__)


def _oid(s):
    try:
        return ObjectId(s)
    except Exception:
        return None


def admin_required(fn):
    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        user_id = get_jwt_identity()
        db = get_db()
        user = db.users.find_one({"_id": _oid(user_id)})
        if not user or user.get("role") != "admin":
            return jsonify({"error": "Admin access required"}), 403
        return fn(*args, **kwargs)
    return wrapper


# ═══════════════════════════════════════════════════════════════════
# ANALYTICS
# ═══════════════════════════════════════════════════════════════════

@admin_bp.route("/analytics", methods=["GET"])
@admin_required
def analytics():
    db = get_db()

    total_users = db.users.count_documents({})

    agg = list(db.users.aggregate([
        {"$group": {"_id": None, "total": {"$sum": "$login_count"}}}
    ]))
    total_logins = agg[0]["total"] if agg else 0

    total_tests_taken = db.progress.count_documents({})
    active_users = db.users.count_documents({"login_count": {"$gt": 0}})

    # Per-user test counts
    per_user_agg = list(db.progress.aggregate([
        {"$group": {"_id": "$user_id", "tests_taken": {"$sum": 1}}},
        {"$sort": {"tests_taken": -1}},
    ]))
    per_user_table = []
    for row in per_user_agg:
        user = db.users.find_one({"_id": row["_id"]}, {"name": 1, "email": 1, "login_count": 1, "last_login": 1})
        if user:
            per_user_table.append({
                "user_id": str(row["_id"]),
                "name": user.get("name", ""),
                "email": user.get("email", ""),
                "tests_taken": row["tests_taken"],
                "login_count": user.get("login_count", 0),
                "last_login": user["last_login"].isoformat() if user.get("last_login") else None,
            })

    return jsonify({
        "total_users": total_users,
        "total_logins": total_logins,
        "total_tests_taken": total_tests_taken,
        "active_users": active_users,
        "per_user_table": per_user_table,
    }), 200


# ═══════════════════════════════════════════════════════════════════
# ALL USERS (admin list)
# ═══════════════════════════════════════════════════════════════════

@admin_bp.route("/users", methods=["GET"])
@admin_required
def list_users():
    db = get_db()
    users = list(db.users.find({}, {"password": 0}))
    for u in users:
        u["_id"] = str(u["_id"])
        if u.get("last_login"):
            u["last_login"] = u["last_login"].isoformat()
        if u.get("created_at"):
            u["created_at"] = u["created_at"].isoformat()
    return jsonify(users), 200


# ═══════════════════════════════════════════════════════════════════
# LANGUAGES
# ═══════════════════════════════════════════════════════════════════

@admin_bp.route("/language", methods=["POST"])
@admin_required
def create_language():
    data = request.get_json() or {}
    name = data.get("language_name", "").strip()
    desc = data.get("description", "").strip()
    if not name:
        return jsonify({"error": "language_name required"}), 400
    db = get_db()
    result = db.languages.insert_one({"language_name": name, "description": desc})
    return jsonify({"message": "Language created", "id": str(result.inserted_id)}), 201


@admin_bp.route("/language/<lang_id>", methods=["PUT"])
@admin_required
def update_language(lang_id):
    data = request.get_json() or {}
    db = get_db()
    update = {}
    if "language_name" in data:
        update["language_name"] = data["language_name"].strip()
    if "description" in data:
        update["description"] = data["description"].strip()
    if not update:
        return jsonify({"error": "Nothing to update"}), 400
    db.languages.update_one({"_id": _oid(lang_id)}, {"$set": update})
    return jsonify({"message": "Language updated"}), 200


@admin_bp.route("/language/<lang_id>", methods=["DELETE"])
@admin_required
def delete_language(lang_id):
    db = get_db()
    db.languages.delete_one({"_id": _oid(lang_id)})
    # Cascade delete topics and questions
    topics = list(db.topics.find({"language_id": _oid(lang_id)}, {"_id": 1}))
    topic_ids = [t["_id"] for t in topics]
    db.questions.delete_many({"topic_id": {"$in": topic_ids}})
    db.topics.delete_many({"language_id": _oid(lang_id)})
    return jsonify({"message": "Language and related data deleted"}), 200


# ═══════════════════════════════════════════════════════════════════
# TOPICS
# ═══════════════════════════════════════════════════════════════════

@admin_bp.route("/topic", methods=["POST"])
@admin_required
def create_topic():
    data = request.get_json() or {}
    language_id = data.get("language_id", "").strip()
    topic_name = data.get("topic_name", "").strip()
    content = data.get("content", "").strip()
    if not language_id or not topic_name:
        return jsonify({"error": "language_id and topic_name required"}), 400
    db = get_db()
    result = db.topics.insert_one({
        "language_id": _oid(language_id),
        "topic_name": topic_name,
        "content": content,
    })
    return jsonify({"message": "Topic created", "id": str(result.inserted_id)}), 201


@admin_bp.route("/topic/<topic_id>", methods=["PUT"])
@admin_required
def update_topic(topic_id):
    data = request.get_json() or {}
    db = get_db()
    update = {}
    for field in ("topic_name", "content"):
        if field in data:
            update[field] = data[field].strip()
    if "language_id" in data:
        update["language_id"] = _oid(data["language_id"])
    if not update:
        return jsonify({"error": "Nothing to update"}), 400
    db.topics.update_one({"_id": _oid(topic_id)}, {"$set": update})
    return jsonify({"message": "Topic updated"}), 200


@admin_bp.route("/topic/<topic_id>", methods=["DELETE"])
@admin_required
def delete_topic(topic_id):
    db = get_db()
    db.questions.delete_many({"topic_id": _oid(topic_id)})
    db.topics.delete_one({"_id": _oid(topic_id)})
    return jsonify({"message": "Topic and questions deleted"}), 200


# ═══════════════════════════════════════════════════════════════════
# QUESTIONS
# ═══════════════════════════════════════════════════════════════════

@admin_bp.route("/question", methods=["POST"])
@admin_required
def create_question():
    data = request.get_json() or {}
    topic_id = data.get("topic_id", "").strip()
    question_text = data.get("question_text", "").strip()
    options = data.get("options", [])
    correct_answer = data.get("correct_answer", "").strip()
    if not topic_id or not question_text or not options or not correct_answer:
        return jsonify({"error": "topic_id, question_text, options, correct_answer required"}), 400
    db = get_db()
    result = db.questions.insert_one({
        "topic_id": _oid(topic_id),
        "question_text": question_text,
        "options": options,
        "correct_answer": correct_answer,
    })
    return jsonify({"message": "Question created", "id": str(result.inserted_id)}), 201


@admin_bp.route("/question/<q_id>", methods=["PUT"])
@admin_required
def update_question(q_id):
    data = request.get_json() or {}
    db = get_db()
    update = {}
    for field in ("question_text", "options", "correct_answer"):
        if field in data:
            update[field] = data[field]
    if "topic_id" in data:
        update["topic_id"] = _oid(data["topic_id"])
    if not update:
        return jsonify({"error": "Nothing to update"}), 400
    db.questions.update_one({"_id": _oid(q_id)}, {"$set": update})
    return jsonify({"message": "Question updated"}), 200


@admin_bp.route("/question/<q_id>", methods=["DELETE"])
@admin_required
def delete_question(q_id):
    db = get_db()
    db.questions.delete_one({"_id": _oid(q_id)})
    return jsonify({"message": "Question deleted"}), 200


# ═══════════════════════════════════════════════════════════════════
# ALL QUESTIONS for a topic (admin view with answers)
# ═══════════════════════════════════════════════════════════════════

@admin_bp.route("/questions/<topic_id>", methods=["GET"])
@admin_required
def admin_get_questions(topic_id):
    db = get_db()
    qs = list(db.questions.find({"topic_id": _oid(topic_id)}))
    for q in qs:
        q["_id"] = str(q["_id"])
        q["topic_id"] = str(q["topic_id"])
    return jsonify(qs), 200
