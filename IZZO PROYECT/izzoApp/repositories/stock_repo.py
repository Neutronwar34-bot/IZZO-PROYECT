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
    def get_or_create(product_id, location_id):
        stock = StockRepository.get(product_id, location_id)
        if not stock:
            stock = Stock(
                product_id=product_id,
                location_id=location_id,
                quantity=0
            )
            db.session.add(stock)
            db.session.flush()  # obtiene id sin commit
        return stock

    @staticmethod
    def set_quantity(stock, quantity):
        stock.quantity = quantity
        db.session.add(stock)
