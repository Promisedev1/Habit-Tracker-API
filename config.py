import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()


class Config:

    # 1. Secret Keys
    SECRET_KEY = os.environ.get("SECRET_KEY")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")

    # 2. JWT Expiration
    jwt_expires = int(os.environ.get("JWT_ACCESS_TOKEN_EXPIRES", 3600))
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=jwt_expires)

    # 3. Database
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False


class TestConfig(Config):
    TESTING = True
    # Use a database that lives only in the computer's RAM
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
