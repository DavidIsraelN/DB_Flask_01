import http
from flask import Blueprint, request
from .services import service_create_user, service_get_all_useres

test_route = Blueprint('user_test', __name__)


# GET - 
@test_route.route('/test', methods=['GET'])
def get_user_test():
    try:
        return service_get_all_useres(), http.HTTPStatus.OK
    
    except Exception as e: 
        return {'error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR


# POST -
@test_route.route('/test', methods=['POST'])
def create_user_test():
    try:
        print(f"data is: { request.get_json() }")
        return service_create_user(request.get_json()), http.HTTPStatus.CREATED

    except Exception as e:
        return {'error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
