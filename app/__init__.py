from flask import Flask, jsonify
from .extensions import db, jwt
from .auth import auth_blueprint
from .habits import habits_blueprint
from .errors import errors_blueprint
from .models import TokenBlocklist


def create_app(config):
    # Initialize the Flask app
    app = Flask(__name__)

    # Load configuration settings
    app.config.from_object(config)

    # Set up the database
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Set up JWT authentication
    jwt.init_app(app)

    @jwt.token_in_blocklist_loader
    def check_if_token_revoked(jwt_header, jwt_payload):
        jti = jwt_payload["jti"]
        token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()
        return token is not None

    # Register blueprints with a shared URL prefix
    app.register_blueprint(auth_blueprint, url_prefix="/api/v1")
    app.register_blueprint(habits_blueprint, url_prefix="/api/v1")
    app.register_blueprint(errors_blueprint)

    # Health check route — confirms the API is up and running
    @app.route("/health", methods=["GET"])
    def health_check():
        return jsonify(status="healthy", message="Habit Tracker API is running"), 200

    return app
