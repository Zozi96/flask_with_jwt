from flask import Flask
from flask_jwt_extended import JWTManager
from apps.web import web as web_blueprint


def create_app(settings_config):
    app = Flask(__name__)
    app.config.from_object(settings_config)
    app.register_blueprint(web_blueprint)
    jwt = JWTManager(app)
    return app
