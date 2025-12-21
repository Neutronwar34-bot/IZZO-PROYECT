from izzoApp.utils.db import db

class Stock(db.Model):
    __tablename__ = "stocks"

    id = db.Column(db.Integer, primary_key=True)

    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable=False)

    quantity = db.Column(db.Integer, default=0, nullable=False)

    product = db.relationship("Product")
    location = db.relationship("Location")

    __table_args__ = (
        db.UniqueConstraint("product_id", "location_id", name="uix_product_location"),
    )
