from .db_utils import Database

class UserRepository:
    def __init__(self):
        self.db = Database()


    def create_user_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(250),
            last_name VARCHAR(250),
            country VARCHAR(250),
            national_id VARCHAR(250),
            phone_number VARCHAR(250)
        );
        """
        self.db.execute_query(query)
    

    def get_all_users(self):
        query = "SELECT * FROM users"
        return self.db.execute_query(query)


    def add_user(self, first_name, last_name, email):
        insert_query = "INSERT INTO users (first_name, last_name, email) VALUES (%s, %s, %s)"
        self.db.execute_query(insert_query, (first_name, last_name, email))
        return {
            'first_name': first_name,
            'last_name': last_name,
            'email': email
        }
        # return {'message': 'Data inserted successfully'}, 201


    # def get_user_by_id(self, user_id):
    #     query = "SELECT * FROM users WHERE id = %s;"
    #     return self.db.execute_query(query, (user_id,))


    # def delete_user(self, user_id):
    #     query = "DELETE FROM users WHERE id = %s;"
    #     self.db.execute_query(query, (user_id,))
    