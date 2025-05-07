from .db_utils import Database

class UserRepository:
    def __init__(self):
        self.db = Database()


    def create_user_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(250),
            last_name VARCHAR(250),
            country VARCHAR(250),
            national_id VARCHAR(250),
            phone_number VARCHAR(250)
        );
        """
        self.db.execute_query(query)
    

    def create_user_role_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS user_role (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL REFERENCES users(id),
            user_type VARCHAR(250) NOT NULL CHECK (user_type IN ('student', 'teacher', 'admin'))
        );
        """
        self.db.execute_query(query)

    
    def get_all_users(self):
        query = "SELECT * FROM users"
        return self.db.execute_query(query)


    def get_user_by_id(self, user_id):
        query = "SELECT * FROM users WHERE id = %s;"
        return self.db.execute_query(query, (user_id,)) # (user_id,) is a tuple with one element
    

    def get_user_with_role_by_id(self, user_id):
        query = """
        SELECT 
            u.id, u.first_name, u.last_name, u.country, u.national_id, u.phone_number,
            ur.user_type
        FROM users u
        LEFT JOIN user_role ur ON u.id = ur.user_id
        WHERE u.id = %s;
        """
        return self.db.execute_query(query, (user_id,))
        # print(f"result (type {type(result)}) is: { result }")
        # return result[0] if result else None


    def get_country_by_user_id(self, user_id):
        query = "SELECT country FROM users WHERE id = %s;"
        return self.db.execute_query(query, (user_id,)) # (user_id,) is a tuple with one element
    

    def add_user(self, first_name, last_name, country, national_id, phone_number):
        query = """
        INSERT INTO users (first_name, last_name, country, national_id, phone_number)
        VALUES (%s, %s, %s, %s, %s) RETURNING id;
        """
        return self.db.execute_query(query, (first_name, last_name, country, national_id, phone_number))[0][0]
    

    def add_user_role(self, user_id, user_type):
        query = """
        INSERT INTO user_role (user_id, user_type)
        VALUES (%s, %s);
        """
        self.db.execute_query(query, (user_id, user_type))


    # def delete_user(self, user_id):
    #     query = "DELETE FROM users WHERE id = %s;"
    #     self.db.execute_query(query, (user_id,))
    