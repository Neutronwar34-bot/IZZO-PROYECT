from izzoApp.utils.db import db
from datetime import datetime


class StockMovement(db.Model):
    __tablename__ = "stock_movements"

    id = db.Column(db.Integer, primary_key=True)

    product_id = db.Column(
        db.Integer,
        db.ForeignKey("products.id"),
        nullable=False
    )

    location_id = db.Column(
        db.Integer,
        db.ForeignKey("locations.id"),
        nullable=False
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    quantity = db.Column(db.Integer, nullable=False)

    movement_type = db.Column(
        db.String(20),
        nullable=False
    )  # IN | OUT | ADJUST

    reference = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    product = db.relationship("Product")
    location = db.relationship("Location")
    user = db.relationship("User")

    def __repr__(self):
        return f"<StockMovement {self.movement_type} {self.quantity}>"
