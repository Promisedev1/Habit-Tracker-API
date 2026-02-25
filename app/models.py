from app.extensions import db
from uuid import uuid4


def generate_id():
    return uuid4().hex


class Habit(db.Model):
    habit_id = db.Column(db.String(32), primary_key=True, default=generate_id)
    name = db.Column(db.String(80), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.String(32), db.ForeignKey("user.user_id"), nullable=False)

    def to_dict(self):
        return {
            "habit_id": self.habit_id,
            "name": self.name,
            "completed": self.completed,
        }


class User(db.Model):
    user_id = db.Column(db.String(32), primary_key=True, default=generate_id)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    habits = db.relationship("Habit", backref="user", lazy=True)

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "email": self.email,
            "username": self.username,
            "habits": [habit.to_dict() for habit in self.habits],
        }


class TokenBlocklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, index=True)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
