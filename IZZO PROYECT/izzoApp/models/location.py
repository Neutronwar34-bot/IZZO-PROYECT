from izzoApp.utils.db import db


class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, server_default=db.func.now())

    stocks = db.relationship(
        "Stock",
        back_populates="location",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Location {self.name}>"

