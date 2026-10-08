from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.db import get_db
from bson import ObjectId
from datetime import datetime

user_bp = Blueprint("user", __name__)


def _oid(s):
    try:
        return ObjectId(s)
    except Exception:
        return None


# ── Languages ───────────────────────────────────────────────────────────────

@user_bp.route("/languages", methods=["GET"])
@jwt_required()
def get_languages():
    db = get_db()
    langs = list(db.languages.find())
    for l in langs:
        l["_id"] = str(l["_id"])
    return jsonify(langs), 200


# ── Topics ───────────────────────────────────────────────────────────────────

@user_bp.route("/topics/<language_id>", methods=["GET"])
@jwt_required()
def get_topics(language_id):
    db = get_db()
    oid = _oid(language_id)
    if not oid:
        return jsonify({"error": "Invalid language_id"}), 400
    topics = list(db.topics.find({"language_id": oid}))
    for t in topics:
        t["_id"] = str(t["_id"])
        t["language_id"] = str(t["language_id"])
    return jsonify(topics), 200


# ── Questions ────────────────────────────────────────────────────────────────

@user_bp.route("/questions/<topic_id>", methods=["GET"])
@jwt_required()
def get_questions(topic_id):
    db = get_db()
    oid = _oid(topic_id)
    if not oid:
        return jsonify({"error": "Invalid topic_id"}), 400
    questions = list(db.questions.find({"topic_id": oid}))
    for q in questions:
        q["_id"] = str(q["_id"])
        q["topic_id"] = str(q["topic_id"])
        # Never send the correct answer to the client before submission
    return jsonify(questions), 200


# ── Submit Quiz ───────────────────────────────────────────────────────────────

@user_bp.route("/submit-quiz", methods=["POST"])
@jwt_required()
def submit_quiz():
    user_id = get_jwt_identity()
    data = request.get_json() or {}
    topic_id = data.get("topic_id")
    answers = data.get("answers", {})   # {question_id: selected_option}

    if not topic_id:
        return jsonify({"error": "topic_id required"}), 400

    db = get_db()
    oid = _oid(topic_id)
    if not oid:
        return jsonify({"error": "Invalid topic_id"}), 400

    questions = list(db.questions.find({"topic_id": oid}))
    if not questions:
        return jsonify({"error": "No questions found for this topic"}), 404

    correct = 0
    total = len(questions)
    results = []
    for q in questions:
        qid = str(q["_id"])
        user_ans = answers.get(qid)
        is_correct = user_ans == q["correct_answer"]
        if is_correct:
            correct += 1
        results.append({
            "question_id": qid,
            "question_text": q["question_text"],
            "your_answer": user_ans,
            "correct_answer": q["correct_answer"],
            "is_correct": is_correct,
        })

    score = round((correct / total) * 100, 2) if total else 0

    db.progress.insert_one({
        "user_id": ObjectId(user_id),
        "topic_id": oid,
        "score": score,
        "correct": correct,
        "total": total,
        "attempt_date": datetime.utcnow(),
    })

    return jsonify({
        "score": score,
        "correct": correct,
        "total": total,
        "results": results,
    }), 200


# ── Progress ─────────────────────────────────────────────────────────────────

@user_bp.route("/progress", methods=["GET"])
@jwt_required()
def get_progress():
    user_id = get_jwt_identity()
    db = get_db()
    records = list(db.progress.find({"user_id": ObjectId(user_id)}))
    for r in records:
        r["_id"] = str(r["_id"])
        r["user_id"] = str(r["user_id"])
        r["topic_id"] = str(r["topic_id"])
        if "attempt_date" in r and r["attempt_date"]:
            r["attempt_date"] = r["attempt_date"].isoformat()
        # Enrich with topic name
        topic = db.topics.find_one({"_id": _oid(r["topic_id"])})
        r["topic_name"] = topic["topic_name"] if topic else "Unknown"
    return jsonify(records), 200
