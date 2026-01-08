from flask import jsonify
from . import v1_blueprint


@v1_blueprint.errorhandler(400)
def bad_request(err):
    return jsonify(error="Bad request", message=str(err.description)), 400


@v1_blueprint.errorhandler(401)
def unauthorized(err):
    return jsonify(error="Unauthorized", message=str(err.description)), 401


@v1_blueprint.errorhandler(404)
def not_found(err):
    return jsonify(error="Not found", message=str(err.description)), 404


@v1_blueprint.errorhandler(429)
def rate_limit_exceeded(err):
    return jsonify(error="Too Many Requests", message=str(err.description)), 429


@v1_blueprint.errorhandler(415)
def unsupported_media_type(err):
    return jsonify(error="Unsupported Media Type", message=str(err.description)), 415


@v1_blueprint.errorhandler(409)
def conflict(err):
    return jsonify(error="Conflict", message=str(err.description)), 409
