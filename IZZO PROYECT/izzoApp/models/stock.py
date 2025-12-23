from izzoApp.utils.db import db
from sqlalchemy import CheckConstraint


class Stock(db.Model):
    __tablename__ = "stocks"

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

    quantity = db.Column(db.Integer, nullable=False, default=0)

    product = db.relationship("Product", back_populates="stocks")
    location = db.relationship("Location", back_populates="stocks")

    __table_args__ = (
        db.UniqueConstraint(
            "product_id",
            "location_id",
            name="uix_product_location"
        ),
        CheckConstraint(
            "quantity >= 0",
            name="ck_stock_quantity_non_negative"
        ),
    )
