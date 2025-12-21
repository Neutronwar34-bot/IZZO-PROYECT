from flask import Blueprint, request, jsonify
from izzoApp.services.report_service import ReportService
from izzoApp.utils.helpers import login_required, role_required

report_bp = Blueprint("reports", __name__, url_prefix="/reports")


@report_bp.route("/kardex", methods=["GET"])
@login_required
@role_required("admin", "manager")
def kardex():
    product_id = request.args.get("product_id", type=int)
    location_id = request.args.get("location_id", type=int)

    if not product_id:
        return jsonify({"error": "product_id is required"}), 400

    data = ReportService.kardex(product_id, location_id)

    return jsonify(data)


@report_bp.route("/stock", methods=["GET"])
@login_required
@role_required("admin", "manager")
def stock_report():
    data = ReportService.stock_report()
    return jsonify(data)
