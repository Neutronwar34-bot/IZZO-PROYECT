from functools import wraps
from flask import request, jsonify, g
from datetime import datetime

from izzoApp.models.authToken import AuthToken
from izzoApp.models.user import User


from functools import wraps
from flask import jsonify, g

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Authorization token required"}), 401

        token_value = auth_header.split(" ")[1]

        auth_token = AuthToken.query.filter_by(token=token_value).first()

        if not auth_token:
            return jsonify({"error": "Invalid token"}), 401

        if auth_token.expires_at and auth_token.expires_at < datetime.utcnow():
            return jsonify({"error": "Token expired"}), 401

        user = User.query.get(auth_token.user_id)

        if not user or not user.is_active:
            return jsonify({"error": "User inactive or not found"}), 401

        # Usuario disponible globalmente durante el request
        g.current_user = user

        return f(*args, **kwargs)

    return decorated_function


def role_required(*allowed_roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user = getattr(g, "current_user", None)

            if not user:
                return jsonify({"error": "Authentication required"}), 401

            user_role = user.role.name if user.role else None

            if user_role not in allowed_roles:
                return jsonify({"error": "Forbidden"}), 403

            return f(*args, **kwargs)

        return decorated_function
    return decorator
