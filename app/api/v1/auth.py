from . import v1_blueprint
from ...extensions import (
    create_access_token,
    db,
    check_password_hash,
    generate_password_hash,
    datetime,
)
from flask import request, jsonify, abort
from ...models import User


# Registration route
@v1_blueprint.route("/register", methods=["POST"])
def register():
    if request.is_json:
        username = request.json.get("username", None)
        password = request.json.get("password", None)

        if not username or not password:
            abort(400, description="Invalid credentials")

        is_existing_user = User.query.filter_by(username=username).first()
        if is_existing_user:
            abort(409, description="Username already exists")
        user = User(username=username, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        return jsonify(message="Registration successfully"), 201
    abort(415)


# Login route
@v1_blueprint.route("/login", methods=["POST"])
def login():
    if request.is_json:
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        if not username or not password:
            abort(400, description="Missing username or password")
        # Only fetches the Id and Password, not the entire User object
        user = (
            db.session.query(User.id, User.password)
            .filter_by(username=username)
            .first()
        )

        if user and check_password_hash(user.password, password):
            access_token = create_access_token(
                identity=str(user.id), expires_delta=datetime.timedelta(minutes=3)
            )
            return jsonify(access_token=access_token), 200

        abort(401, description="Invalid credentials")

    abort(415)
