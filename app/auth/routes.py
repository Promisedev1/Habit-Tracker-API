from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from datetime import timedelta
from app.extensions import db
from app.schemas import RegisterUser, LoginUser
from app.models import TokenBlocklist
from .services import AuthService


auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/register", methods=["POST"])
def register():
    body = RegisterUser(**request.get_json())

    user, error = AuthService.create_user(body.email, body.username, body.password)
    if error:
        status = 409 if "exists" in error else 500
        abort(status, description=error)

    return jsonify(message="Registration successful"), 201


@auth_blueprint.route("/login", methods=["POST"])
def login():
    body = LoginUser(**request.get_json())

    user = AuthService.verify_credentials(body.email, body.password)
    if not user:
        abort(401, description="Invalid credentials")

    token = create_access_token(
        identity=str(user.user_id), expires_delta=timedelta(minutes=30)
    )
    return jsonify(access_token=token), 200


@auth_blueprint.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    db.session.add(TokenBlocklist(jti=jti))
    db.session.commit()
    return jsonify(message="Successfully logged out"), 200
