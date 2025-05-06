from flask import Blueprint, jsonify, request
from .db_utils import Database


test_route = Blueprint('test', __name__)


# GET - 
@test_route.route('/', methods=['GET'])
def get_test():
    try:
        db = Database()
        data = db.execute_query("SELECT * FROM users")
        print(f"data is: { data }")
        # return {'data': data}, 200
        return jsonify(data), 200
    except Exception as e: 
        return {'error': str(e)}, 500


# POST -
@test_route.route('/', methods=['POST'])
def post_test():
    try:
        db = Database()
        data = request.get_json()
        print(f"data is: { data }")

        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')

        if not first_name or not last_name or not email:
            return {'error': 'Missing required fields'}, 400
        
        # Assuming you have a function to insert data into the database
        insert_query = """
            INSERT INTO users (first_name, last_name, email)
            VALUES (%s, %s, %s)
        """
        db.execute_query(insert_query, (first_name, last_name, email))
        # return the new data as a response 
        return {
            'first_name': first_name,
            'last_name': last_name,
            'email': email
        }
        # return {'message': 'Data inserted successfully'}, 201
    except Exception as e:
        return {'error': str(e)}, 500
