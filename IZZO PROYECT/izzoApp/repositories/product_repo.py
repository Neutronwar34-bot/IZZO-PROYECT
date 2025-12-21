from izzoApp.models.product import Product
from izzoApp.utils.db import db


class ProductRepository:

    @staticmethod
    def get_all(active_only=True):
        query = Product.query
        if active_only:
            query = query.filter_by(is_active=True)
        return query.all()

    @staticmethod
    def get_by_id(product_id: int):
        return Product.query.get(product_id)

    @staticmethod
    def get_by_sku(sku: str):
        return Product.query.filter_by(sku=sku).first()

    @staticmethod
    def create(data: dict):
        product = Product(**data)
        db.session.add(product)
        db.session.commit()
        return product

    @staticmethod
    def update(product: Product, data: dict):
        for key, value in data.items():
            setattr(product, key, value)
        db.session.commit()
        return product

    @staticmethod
    def deactivate(product: Product):
        product.is_active = False
        db.session.commit()
