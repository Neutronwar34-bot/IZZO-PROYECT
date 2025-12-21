# app/services/auth_service.py
import uuid
from datetime import datetime, timedelta

from izzoApp.models.user import User
from izzoApp.models.role import Role
from izzoApp.models.authToken import AuthToken
from izzoApp.utils.db import db
from izzoApp.utils.security import hash_password, verify_password


class AuthService:

    @staticmethod
    def register_user(email: str, password: str, role_name: str = "user"):
        if User.query.filter_by(email=email).first():
            raise ValueError("Email already registered")

        role = Role.query.filter_by(name=role_name).first()
        if not role:
            raise ValueError("Role not found")

        user = User(
            email=email,
            password_hash=hash_password(password),
            role_id=role.id
        )

        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def login(email: str, password: str):
        user = User.query.filter_by(email=email, is_active=True).first()
        if not user or not verify_password(password, user.password_hash):
            raise ValueError("Invalid credentials")

        token_value = str(uuid.uuid4())

        token = AuthToken(
            token=token_value,
            user_id=user.id,
            expires_at=datetime.utcnow() + timedelta(hours=8)
        )

        db.session.add(token)
        db.session.commit()

        return token

    @staticmethod
    def logout(token_value: str):
        token = AuthToken.query.filter_by(token=token_value).first()
        if token:
            db.session.delete(token)
            db.session.commit()
