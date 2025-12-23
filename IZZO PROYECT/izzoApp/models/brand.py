from izzoApp.utils.db import db
# izzoApp/models/brand.py
class Brand(db.Model):
    __tablename__ = "brands"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    
    products = db.relationship(
        "Product",
        back_populates="brand",
        cascade="all, delete-orphan"
    )