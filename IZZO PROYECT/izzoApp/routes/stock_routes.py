from flask import Blueprint, request, jsonify, g
from izzoApp.services.stock_service import StockService
from izzoApp.utils.helpers import login_required, role_required

stock_bp = Blueprint("stock", __name__, url_prefix="/stock")


@stock_bp.route("/adjust", methods=["POST"])
@login_required
@role_required("admin", "manager")
def adjust_stock():
    data = request.get_json()

    required = ["product_id", "location_id", "quantity", "movement_type"]
    if not data or not all(k in data for k in required):
        return jsonify({"error": "Missing fields"}), 400

    try:
        stock = StockService.adjust_stock(
            product_id=data["product_id"],
            location_id=data["location_id"],
            quantity=data["quantity"],
            movement_type=data["movement_type"],
            user_id=g.current_user.id,
            reference=data.get("reference")
        )

        return jsonify({
            "product_id": stock.product_id,
            "location_id": stock.location_id,
            "quantity": stock.quantity
        })

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
