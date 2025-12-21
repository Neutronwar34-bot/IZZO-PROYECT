from izzoApp.utils.db import db

class Brand(db.Model):
    __tablename__ = "brands"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    products = db.relationship("Product", back_populates="brand")

    def __repr__(self):
        return f"<Brand {self.name}>"
