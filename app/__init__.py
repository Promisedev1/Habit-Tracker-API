from flask import Flask, jsonify
from .api.v1 import v1_blueprint
from .extensions import JWTManager, limiter, db


def create_app(config):
    # Initialize the Flask object
    app = Flask(__name__)

    # Configuration settings
    app.config.from_object(config)

    # Database initialization
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Initialize JWT Manager for handling JWTs
    jwt = JWTManager(app)

    # Initialize the limiter
    limiter.init_app(app)

    # Register the v1 blueprint
    app.register_blueprint(v1_blueprint, url_prefix="/api/v1")

    # A simple Health Check route
    # We put this here just to verify the factory works.
    @app.route("/health", methods=["GET"])
    def health_check():
        return jsonify(status="healthy", message="Habit Tracker API is running"), 200

    # Return the app object
    return app
