from flask import Blueprint, request, jsonify
from izzoApp.services.product_service import ProductService
from izzoApp.utils.helpers import login_required, role_required

product_bp = Blueprint("products", __name__, url_prefix="/products")


@product_bp.route("/", methods=["GET"])
@login_required
def list_products():
    products = ProductService.list_products()

    return jsonify([
        {
            "id": p.id,
            "sku": p.sku,
            "name": p.name,
            "price": str(p.price),
            "category_id": p.category_id,
            "brand_id": p.brand_id
        }
        for p in products
    ])


@product_bp.route("/", methods=["POST"])
@login_required
@role_required("admin", "manager")
def create_product():
    data = request.get_json()

    required_fields = ["sku", "name", "price", "category_id"]
    if not data or not all(field in data for field in required_fields):
        return jsonify({"error": "Missing fields"}), 400

    try:
        product = ProductService.create_product(data)
        return jsonify({"id": product.id}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@product_bp.route("/<int:product_id>", methods=["PUT"])
@login_required
@role_required("admin", "manager")
def update_product(product_id):
    data = request.get_json()

    try:
        ProductService.update_product(product_id, data)
        return jsonify({"message": "Product updated"})
    except ValueError as e:
        return jsonify({"error": str(e)}), 404



