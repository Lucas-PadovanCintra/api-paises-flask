import logging
import os
import time
from flask import Flask, request, g
from config import DevelopmentConfig, ProductionConfig, TestingConfig
from exceptions import (
    BusinessError,
    ResourceNotFoundError,
    ExternalAPIError
)
from werkzeug.exceptions import HTTPException
from app.pais.routes import pais_bp
from app.health.routes import health_bp
from logging_config import JsonFormatter


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = JsonFormatter()
handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(handler)


def create_app():

    app = Flask(__name__)
    env = os.getenv("FLASK_ENV", "development")

    if env == "production":
        app.config.from_object(ProductionConfig)
    elif    env == "testing":
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    app.register_blueprint(pais_bp)
    app.register_blueprint(health_bp)

    @app.before_request
    def start_timer():
        g.start_time = time.time()

        logger.info(
            "Request iniciada",
            extra={
                "event": "request_started",
                "method": request.method,
                "path": request.path
            }
        )

    @app.after_request
    def log_response(response):
        duration = time.time() - g.start_time

        logger.info(
            "Request finalizada",
            extra={
                "event": "request_finished",
                "method": request.method,
                "path": request.path,
                "status_code": response.status_code,
                "duration_ms": round(duration * 1000, 2)
            }
        )

        return response

    @app.errorhandler(ResourceNotFoundError)
    def handle_resource_not_found(error):
        logger.warning(
            "Recurso não encontrado",
            extra={
                "event": "resource_not_found",
                "error_type": "RESOURCE_NOT_FOUND"
            }
        )
        return error.to_dict(), 404

    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        logger.warning(
            "Erro HTTP",
            extra={
                "event": "http_exception",
                "error_type": error.name.upper().replace(" ", "_")
            }
        )
        return {
            "error": {
                "type": error.name.upper().replace(" ", "_"),
                "message": error.description
            }
        }, error.code

    @app.errorhandler(ExternalAPIError)
    def handle_external_api_error(error):
        logger.error(
            "Erro externo",
            extra={
                "event": "external_api_error",
                "error_type": "EXTERNAL_API_ERROR"
            }
        )
        return error.to_dict(), 502

    @app.errorhandler(BusinessError)
    def handle_business_error(error):
        logger.warning(
            "Erro de regra",
            extra={
                "event": "business_error",
                "error_type": "BUSINESS_ERROR"
            }
        )
        return error.to_dict(), 400

    @app.errorhandler(Exception)
    def handle_generic_error(error):
        logger.exception(
            "Erro inesperado",
            extra={
                "event": "internal_error",
                "error_type": "INTERNAL_ERROR"
            }
        )
        return {
            "error": {
                "type": "INTERNAL_ERROR",
                "message": "Erro interno"
            }
        }, 500

    return app
