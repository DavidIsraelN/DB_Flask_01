from flask import Flask
from .routes import test_route as test_bp


def create_app():
    app = Flask(__name__)


    # app.register_blueprint(test_bp, url_prefix='/test')
    app.register_blueprint(test_bp)
    

    return app
