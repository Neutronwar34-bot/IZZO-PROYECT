from izzoApp.repositories.movement_repo import MovementRepository

class ReportService:

    @staticmethod
    def kardex(product_id: int, location_id: int = None):
        movements = MovementRepository.list_by_product(
            product_id=product_id,
            location_id=location_id
        )

        return [
            {
                "date": m.created_at.isoformat(),
                "type": m.movement_type,
                "quantity": m.quantity,
                "location_id": m.location_id,
                "reference": m.reference,
                "user_id": m.user_id
            }
            for m in movements
        ]

    @staticmethod
    def stock_report():
        stocks = MovementRepository.stock_snapshot()

        return [
            {
                "product_id": s.product_id,
                "location_id": s.location_id,
                "quantity": s.quantity
            }
            for s in stocks
        ]
