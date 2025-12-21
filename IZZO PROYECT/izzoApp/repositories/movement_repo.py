from izzoApp.models.stock_movement import StockMovement
from izzoApp.utils.db import db


from izzoApp.models.stock import Stock

class MovementRepository:

    @staticmethod
    def create(data: dict):
        movement = StockMovement(**data)
        db.session.add(movement)
        db.session.commit()
        return movement

    @staticmethod
    def list_by_product(product_id):
        return StockMovement.query.filter_by(product_id=product_id).order_by(
            StockMovement.created_at.desc()
        ).all()




class MovementRepository:

    @staticmethod
    def list_by_product(product_id, location_id=None):
        query = StockMovement.query.filter_by(product_id=product_id)

        if location_id:
            query = query.filter_by(location_id=location_id)

        return query.order_by(StockMovement.created_at.asc()).all()

    @staticmethod
    def stock_snapshot():
        return Stock.query.all()
