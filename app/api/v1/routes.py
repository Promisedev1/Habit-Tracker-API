from flask import abort, jsonify, request
from . import v1_blueprint
from ...extensions import jwt_required, limiter, db, get_jwt_identity
from ...models import Habit, User


# 3. Define the RESTful Routes
@v1_blueprint.route("/habits", methods=["GET"])
@limiter.limit("5 per minute")
@jwt_required()
def get_habits():
    # All habit that belongs to the user
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    if not user:
        abort(404, description="User not found")

    habits_list = [
        habit.to_dict()
        for habit in Habit.query.filter_by(user_id=current_user_id).all()
    ]
    return jsonify(habits=habits_list), 200


@v1_blueprint.route("/habits/<int:id>", methods=["GET"])
@jwt_required()
def get_single_habit(id):
    habit = Habit.query.get(id)
    if habit is None:
        abort(404, description="Habit not found")
    return jsonify(habit.to_dict()), 200


@v1_blueprint.route("/habits", methods=["POST"])
@jwt_required()
def create_habit():

    if request.is_json:
        data = request.json.get("name", None)
        if data is None:
            abort(400, description="Missing 'name' in request data")

        # Create a new habit
        current_user_id = get_jwt_identity()
        new_habit = Habit(name=data, user_id=current_user_id)
        db.session.add(new_habit)
        db.session.commit()
        return jsonify(new_habit.to_dict()), 201

    abort(415, description="Content type must be application/json")
