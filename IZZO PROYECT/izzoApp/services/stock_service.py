from izzoApp.repositories.stock_repo import StockRepository
from izzoApp.repositories.movement_repo import MovementRepository

class StockService:

    @staticmethod
    def adjust_stock(
        product_id: int,
        location_id: int,
        quantity: int,
        movement_type: str,
        user_id: int,
        reference: str = None
    ):
        stock = StockRepository.get(product_id, location_id)

        if not stock:
            stock = StockRepository.create(product_id, location_id, 0)

        if movement_type == "IN":
            new_quantity = stock.quantity + quantity
        elif movement_type == "OUT":
            if stock.quantity < quantity:
                raise ValueError("Insufficient stock")
            new_quantity = stock.quantity - quantity
        elif movement_type == "ADJUST":
            new_quantity = quantity
        else:
            raise ValueError("Invalid movement type")

        StockRepository.update(stock, new_quantity)

        MovementRepository.create({
            "product_id": product_id,
            "location_id": location_id,
            "quantity": quantity,
            "movement_type": movement_type,
            "user_id": user_id,
            "reference": reference
        })

        return stock
