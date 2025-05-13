from flask import Flask
from app.routes.user_routes import user_bp
from app.routes.sms_routes import sms_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(sms_bp, url_prefix='/sms')

    return app
