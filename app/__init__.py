from flask import Flask
# from .db_utils import get_db_connection
# from .routes import bp as main_bp


def create_app():
    app = Flask(__name__)

    # app.config.from_object('config.Config')

    # try:
    #     conn = get_db_connection()
    #     print("Database connection successful!")
    # except Exception as e:
    #     print("Database connection failed:", e)

    # app.register_blueprint(main_bp)

    return app
