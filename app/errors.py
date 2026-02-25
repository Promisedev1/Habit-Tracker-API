from flask import Blueprint, jsonify
from werkzeug.exceptions import (
    BadRequest,
    Unauthorized,
    NotFound,
    Conflict,
    UnsupportedMediaType,
    TooManyRequests,
    InternalServerError,
)

from pydantic import ValidationError

errors_blueprint = Blueprint("errors", __name__)


@errors_blueprint.app_errorhandler(ValidationError)
def validation_error(err):
    return jsonify(error="Validation Error", message=err.errors()), 422


@errors_blueprint.app_errorhandler(BadRequest)
def bad_request(err):
    return jsonify(error="Bad Request", message=str(err.description)), 400


@errors_blueprint.app_errorhandler(Unauthorized)
def unauthorized(err):
    return jsonify(error="Unauthorized", message=str(err.description)), 401


@errors_blueprint.app_errorhandler(NotFound)
def not_found(err):
    return jsonify(error="Not Found", message=str(err.description)), 404


@errors_blueprint.app_errorhandler(Conflict)
def conflict(err):
    return jsonify(error="Conflict", message=str(err.description)), 409


@errors_blueprint.app_errorhandler(UnsupportedMediaType)
def unsupported_media_type(err):
    return jsonify(error="Unsupported Media Type", message=str(err.description)), 415


@errors_blueprint.app_errorhandler(TooManyRequests)
def rate_limit_exceeded(err):
    return (
        jsonify(
            error="Too Many Requests",
            message=str(err.description),
            retry_after=getattr(err, "retry_after", None),
        ),
        429,
    )


@errors_blueprint.app_errorhandler(InternalServerError)
def internal_server_error(err):
    return jsonify(error="Internal Server Error", message=str(err.description)), 500
