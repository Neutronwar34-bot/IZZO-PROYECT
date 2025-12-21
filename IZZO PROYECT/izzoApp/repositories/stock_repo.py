from izzoApp.models.stock import Stock
from izzoApp.utils.db import db

class StockRepository:

    @staticmethod
    def get(product_id, location_id):
        return Stock.query.filter_by(
            product_id=product_id,
            location_id=location_id
        ).first()

    @staticmethod
    def create(product_id, location_id, quantity=0):
        stock = Stock(
            product_id=product_id,
            location_id=location_id,
            quantity=quantity
        )
        db.session.add(stock)
        db.session.commit()
        return stock

    @staticmethod
    def update(stock, quantity):
        stock.quantity = quantity
        db.session.commit()
        return stock
