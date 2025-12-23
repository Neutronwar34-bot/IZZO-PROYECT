from izzoApp.utils.db import db
from flask import Flask


def create_app(config_object=None):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)

    with app.app_context():
        # 🔥 OBLIGATORIO: registrar modelos
        import izzoApp.models

        # 🔥 OBLIGATORIO: crear tablas
        db.create_all()

    from izzoApp.routes.auth_routes import auth_bp
    from izzoApp.routes.product_routes import product_bp
    from izzoApp.routes.stock_routes import stock_bp
    from izzoApp.routes.report_routes import report_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(stock_bp)
    app.register_blueprint(report_bp)

    return app


