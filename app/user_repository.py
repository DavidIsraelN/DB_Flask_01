from .db_connection import Database

from config import ALLOWED_ROLES


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
    

    # def create_user_role_table(self):
    #     query = f"""
    #     CREATE TABLE IF NOT EXISTS user_role (
    #         id SERIAL PRIMARY KEY,
    #         user_id INTEGER NOT NULL REFERENCES users(id),
    #         user_type VARCHAR(250) NOT NULL CHECK (user_type IN  {tuple(ALLOWED_ROLES)})
    #     );
    #     """
    #     self.db.execute_query(query)

    
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
        return self.db.execute_query(query, (user_id,)) # (user_id,) is a tuple with one element


    def get_country_by_user_id(self, user_id):
        query = "SELECT country FROM users WHERE id = %s;"
        return self.db.execute_query(query, (user_id,)) # (user_id,) is a tuple with one element
    

    def add_user(self, **user_data):
        fields = ', '.join(user_data.keys())
        placeholders = ', '.join(['%s'] * len(user_data))
        params = tuple(user_data.values())
        query = f"""
        INSERT INTO users ({fields})
        VALUES ({placeholders}) RETURNING id;
        """
        return self.db.execute_query(query, params)[0][0]
    

    def update_user(self, user_id, user_updates):
        set_clause = ", ".join(f"{key} = %s" for key in user_updates.keys())
        query = f"UPDATE users SET {set_clause} WHERE id = %s"
        params = list(user_updates.values()) + [user_id]
        self.db.execute_query(query, params)


    # def delete_user(self, user_id):
    #     query = "DELETE FROM users WHERE id = %s;"
    #     self.db.execute_query(query, (user_id,))
    