from izzoApp.utils.db import db
from izzoApp.models.stock import Stock
from izzoApp.models.stock_movement import StockMovement


class StockService:

    @staticmethod
    def get_or_create_stock(product_id: int, location_id: int) -> Stock:
        stock = Stock.query.filter_by(
            product_id=product_id,
            location_id=location_id
        ).first()

        if not stock:
            stock = Stock(
                product_id=product_id,
                location_id=location_id,
                quantity=0
            )
            db.session.add(stock)
            db.session.flush()  # asegura ID sin commit

        return stock

    # ──────────────────────────────
    # ➕ ENTRADA DE STOCK
    # ──────────────────────────────
    @staticmethod
    def stock_in(
        *,
        product_id: int,
        location_id: int,
        quantity: int,
        user_id: int,
        reference: str | None = None
    ) -> Stock:

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        stock = StockService.get_or_create_stock(product_id, location_id)
        stock.quantity += quantity

        movement = StockMovement(
            product_id=product_id,
            location_id=location_id,
            quantity=quantity,
            movement_type="IN",
            user_id=user_id,
            reference=reference
        )

        db.session.add(movement)
        db.session.commit()

        return stock

    # ──────────────────────────────
    # ➖ SALIDA DE STOCK
    # ──────────────────────────────
    @staticmethod
    def stock_out(
        *,
        product_id: int,
        location_id: int,
        quantity: int,
        user_id: int,
        reference: str | None = None
    ) -> Stock:

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        stock = StockService.get_or_create_stock(product_id, location_id)

        if stock.quantity < quantity:
            raise ValueError("Insufficient stock")

        stock.quantity -= quantity

        movement = StockMovement(
            product_id=product_id,
            location_id=location_id,
            quantity=quantity,
            movement_type="OUT",
            user_id=user_id,
            reference=reference
        )

        db.session.add(movement)
        db.session.commit()

        return stock

    # ──────────────────────────────
    # ♻ AJUSTE DE STOCK
    # ──────────────────────────────
    @staticmethod
    def adjust_stock(
        *,
        product_id: int,
        location_id: int,
        new_quantity: int,
        user_id: int,
        reference: str | None = None
    ) -> Stock:

        if new_quantity < 0:
            raise ValueError("Stock cannot be negative")

        stock = StockService.get_or_create_stock(product_id, location_id)

        diff = new_quantity - stock.quantity

        movement_type = "ADJUST"
        movement_quantity = abs(diff)

        stock.quantity = new_quantity

        movement = StockMovement(
            product_id=product_id,
            location_id=location_id,
            quantity=movement_quantity,
            movement_type=movement_type,
            user_id=user_id,
            reference=reference
        )

        db.session.add(movement)
        db.session.commit()

        return stock
