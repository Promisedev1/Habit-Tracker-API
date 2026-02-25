from flask import Blueprint, abort, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.schemas import CreateHabit, UpdateHabit
from .services import HabitService


habits_blueprint = Blueprint("habits", __name__)


# Get all habits for the logged-in user
@habits_blueprint.route("/habits", methods=["GET"])
@jwt_required()
def get_habits():
    user_id = get_jwt_identity()
    habits, error = HabitService.get_user_habits(user_id)
    if error:
        abort(404, description=error)
    return jsonify(habits=[h.to_dict() for h in habits]), 200


# Get a single habit by id
@habits_blueprint.route("/habits/<string:habit_id>", methods=["GET"])
@jwt_required()
def get_single_habit(habit_id):
    habit = HabitService.get_habit(habit_id)
    if not habit:
        abort(404, description="Habit not found")
    return jsonify(habit.to_dict()), 200


# Create a new habit
@habits_blueprint.route("/habits", methods=["POST"])
@jwt_required()
def create_habit():
    body = CreateHabit(**request.get_json())
    user_id = get_jwt_identity()
    habit, error = HabitService.create_habit(body.name, user_id)
    if error:
        abort(500, description=error)
    return jsonify(habit.to_dict()), 201


# Update an existing habit
@habits_blueprint.route("/habits/<string:habit_id>", methods=["PUT"])
@jwt_required()
def update_habit(habit_id):
    body = UpdateHabit(**request.get_json())
    habit, error = HabitService.update_habit(habit_id, body.name)
    if error:
        abort(404, description=error)
    return jsonify(habit.to_dict()), 200


# Delete a habit
@habits_blueprint.route("/habits/<string:habit_id>", methods=["DELETE"])
@jwt_required()
def delete_habit(habit_id):
    _, error = HabitService.delete_habit(habit_id)
    if error:
        abort(404, description=error)
    return jsonify(message="Habit deleted successfully"), 204
