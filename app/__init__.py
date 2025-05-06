from flask import Flask
from .test_routes import test_bp
from .user_routes import user_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(test_bp, url_prefix='/test')
    app.register_blueprint(user_bp, url_prefix='/users')

    return app
