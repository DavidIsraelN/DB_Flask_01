import http
from flask import Blueprint, request
from .user_service import UserService

test_bp = Blueprint('user_test', __name__)
user_service = UserService()


# GET - 
@test_bp.route('', methods=['GET'])
def get_user_test():
    try:
        return user_service.get_all_users(), http.HTTPStatus.OK
    
    except Exception as e: 
        return {'error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR


# POST -
@test_bp.route('', methods=['POST'])
def create_user_test():
    try:
        print(f"data is: { request.get_json() }")
        return user_service.add_user(request.get_json()), http.HTTPStatus.CREATED

    except Exception as e:
        return {'error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
