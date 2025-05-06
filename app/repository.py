from .db_utils import Database


def repository_get_all_users():
    db = Database()
    select_query = """SELECT * FROM users"""
    return db.execute_query(select_query)


def repository_create_user(first_name, last_name, email):
    db = Database()
    insert_query = """INSERT INTO users (first_name, last_name, email) VALUES (%s, %s, %s)"""
    db.execute_query(insert_query, (first_name, last_name, email))
    return {
        'first_name': first_name,
        'last_name': last_name,
        'email': email
    }
    # return {'message': 'Data inserted successfully'}, 201
