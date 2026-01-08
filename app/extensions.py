from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# We create the object, but don't "attach" it to the app yet
limiter = Limiter(key_func=get_remote_address, storage_uri="memory://")

from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

#import datetime for token expiration
import datetime

#Initialize SQLAlchemy object
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#Werkzeug Security for password hashing
from werkzeug.security import generate_password_hash, check_password_hash
