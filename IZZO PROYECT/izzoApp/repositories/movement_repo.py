from izzoApp.models.stock_movement import StockMovement
from izzoApp.utils.db import db


class MovementRepository:

    @staticmethod
    def create(
        product_id: int,
        location_id: int,
        quantity: int,
        movement_type: str,
        user_id: int,
        reference: str = None
    ):
        movement = StockMovement(
            product_id=product_id,
            location_id=location_id,
            quantity=quantity,
            movement_type=movement_type,
            user_id=user_id,
            reference=reference
        )

        db.session.add(movement)
        return movement

    @staticmethod
    def list_by_product(product_id: int, location_id: int = None):
        query = StockMovement.query.filter_by(product_id=product_id)

        if location_id:
            query = query.filter_by(location_id=location_id)

        return query.order_by(StockMovement.created_at.asc()).all()
