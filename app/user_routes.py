import http
from flask import Blueprint, request
from .user_service import UserService

user_bp = Blueprint('user', __name__)
user_service = UserService()


# POST - route to create user table
@user_bp.route('/create_user_table', methods=['POST'])
def create_user_table():
    try:
        user_service.create_user_table()
        return {"message": "User table created successfully."}, http.HTTPStatus.CREATED
    
    except Exception as e:
        return {"error": str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR


# POST - route to create user role table
@user_bp.route('/create_user_role_table', methods=['POST'])
def create_user_role_table():
    try:
        user_service.create_user_role_table()
        return {"message": "User role table created successfully."}, http.HTTPStatus.CREATED
    
    except Exception as e:
        return {"error": str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR


# GET - route to get all users
@user_bp.route('', methods=['GET'])
def get_users():
    try:
        # return jsonify(user_service.get_all_users()), http.HTTPStatus.OK
        return user_service.get_all_users(), http.HTTPStatus.OK
    
    except Exception as e:
        return {"error": str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR


# GET - route to get user with role by ID in the URL
@user_bp.route('/get_user_with_role/<int:user_id>', methods=['GET'])
def get_user_with_role(user_id):
    try:
        return user_service.get_user_with_role(user_id), http.HTTPStatus.OK
    
    except ValueError as e:
        return {"error": str(e)}, http.HTTPStatus.BAD_REQUEST
    except Exception as e:
        return {"error": str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR


# GET - route to get country code by user ID in the query string
@user_bp.route('/get_country_code', methods=['GET'])
def get_country_code():
    try:
        return user_service.get_country_code(request.args.get('user_id')), http.HTTPStatus.OK        
        
    except ValueError as e:
        return {"error": str(e)}, http.HTTPStatus.BAD_REQUEST
    except Exception as e:
        return {"error": str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR


# # GET - route to get user by ID in the URL
# @user_bp.route('/<int:user_id>', methods=['GET'])
# def get_user(user_id):
#     try:
#         return jsonify(user_service.get_user_by_id(user_id)), http.HTTPStatus.OK
#     except ValueError as e:
#         return {"error": str(e)}, http.HTTPStatus.NOT_FOUND
#     except Exception as e:
#         return {"error": str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR


# POST - route to add a new user
@user_bp.route('/add_user', methods=['POST'])
def add_user():
    try:
        print(f"data is: { request.get_json() }")
        return user_service.add_user(request.get_json()), http.HTTPStatus.CREATED
    
    except ValueError as e:
        return {"error": str(e)}, http.HTTPStatus.BAD_REQUEST
    except Exception as e:
        return {"error": str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR


# POST - route to add a new user with a specific role
@user_bp.route('/add_user_with_role', methods=['POST'])
def add_user_with_role():
    """
    Add a new user with a specific role. request.get_json() should contain user and role.
    :user: Dictionary containing user data (first_name, last_name, country, national_id, phone_number).
    :role: The role to assign to the user (e.g., 'student', 'teacher', 'admin').
    """
    try:
        print(f"data is: { request.get_json() }")
        return user_service.add_user_with_role(request.get_json()), http.HTTPStatus.CREATED

    except ValueError as e:
        return {"error": str(e)}, http.HTTPStatus.BAD_REQUEST
    except Exception as e:
        return {"error": str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR


# # DELETE - route to delete a user by ID in the URL
# @user_bp.route('/<int:user_id>', methods=['DELETE'])
# def delete_user(user_id):
#     try:
#         user_service.delete_user(user_id)
#         return {"message": "User deleted successfully."}, http.HTTPStatus.OK
    
#     except ValueError as e:
#         return {"error": str(e)}, http.HTTPStatus.NOT_FOUND
#     except Exception as e:
#         return {"error": str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
