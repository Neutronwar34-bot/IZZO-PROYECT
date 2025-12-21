# app/routes/auth_routes.py
from flask import Blueprint, request, jsonify

from izzoApp.services.auth_service import AuthService

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    email = data.get("email")
    password = data.get("password")
    role = data.get("role", "user")

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    try:
        user = AuthService.register_user(email, password, role)
        return jsonify({
            "id": user.id,
            "email": user.email,
            "role": role
        }), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400



@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    try:
        token = AuthService.login(email, password)

        return jsonify({
            "token": token.token,
            "expires_at": token.expires_at.isoformat()
        }), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 401


