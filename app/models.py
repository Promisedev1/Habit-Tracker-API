from app.extensions import db
import uuid


def get_id():
    return uuid.uuid4().hex


class Habit(db.Model):
    id = db.Column(db.String(32), primary_key=True, default=get_id)
    name = db.Column(db.String(80), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "completed": self.completed}


class User(db.Model):
    id = db.Column(db.String(32), primary_key=True, default=get_id)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    habits = db.relationship("Habit", backref="user", lazy=True)
