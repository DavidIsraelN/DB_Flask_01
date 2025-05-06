import http
from flask import Blueprint, request
from .user_service import UserService

test_route = Blueprint('user_test', __name__)


# GET - 
@test_route.route('/test', methods=['GET'])
def get_user_test():
    try:
        return UserService.get_all_users(), http.HTTPStatus.OK
    
    except Exception as e: 
        return {'error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR


# POST -
@test_route.route('/test', methods=['POST'])
def create_user_test():
    try:
        print(f"data is: { request.get_json() }")
        return UserService.add_user(request.get_json()), http.HTTPStatus.CREATED

    except Exception as e:
        return {'error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
