from izzoApp.utils.db import db
from datetime import datetime

class AuthToken(db.Model):
    __tablename__ = "auth_tokens"

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(255), unique=True, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=True)

    user = db.relationship("User", back_populates="tokens")

    def __repr__(self):
        return f"<AuthToken user_id={self.user_id}>"
