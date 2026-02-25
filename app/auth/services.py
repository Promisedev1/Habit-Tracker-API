from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db
from app.models import User


class AuthService:
    """Service class for authentication-related operations"""

    @staticmethod
    def create_user(email: str, username: str, password: str):
        if User.query.filter_by(email=email).first():
            return None, "Email already exists"
        if User.query.filter_by(username=username).first():
            return None, "Username already exists"

        hashed_pw = generate_password_hash(password)
        user = User(email=email, username=username, password=hashed_pw)

        try:
            db.session.add(user)
            db.session.commit()
            return user, None
        except Exception:
            db.session.rollback()
            return None, "Database error"

    @staticmethod
    def verify_credentials(email: str, password: str):
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            return user
        return None
