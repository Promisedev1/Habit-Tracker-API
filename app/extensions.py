from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Extension instances — created here, initialised in app/__init__.py
db = SQLAlchemy()
jwt = JWTManager()