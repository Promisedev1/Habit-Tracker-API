from app.extensions import db
from app.models import Habit, User


class HabitService:
    """Service class for habit-related operations"""

    @staticmethod
    def get_user_habits(user_id: str):
        user = User.query.get(user_id)
        if not user:
            return None, "User not found"
        habits = Habit.query.filter_by(user_id=user_id).all()
        return habits, None

    @staticmethod
    def get_habit(habit_id: str):
        return Habit.query.get(habit_id)

    @staticmethod
    def create_habit(name: str, user_id: str):
        habit = Habit(name=name, user_id=user_id)
        try:
            db.session.add(habit)
            db.session.commit()
            return habit, None
        except Exception:
            db.session.rollback()
            return None, "Database error"

    @staticmethod
    def update_habit(habit_id: str, name: str):
        habit = Habit.query.get(habit_id)
        if not habit:
            return None, "Habit not found"
        habit.name = name
        try:
            db.session.commit()
            return habit, None
        except Exception:
            db.session.rollback()
            return None, "Database error"

    @staticmethod
    def delete_habit(habit_id: str):
        habit = Habit.query.get(habit_id)
        if not habit:
            return None, "Habit not found"
        try:
            db.session.delete(habit)
            db.session.commit()
            return True, None
        except Exception:
            db.session.rollback()
            return None, "Database error"
