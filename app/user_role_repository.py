from .db_connection import Database

from config import ALLOWED_ROLES


class UserRoleRepository:
    def __init__(self):
        self.db = Database()
    

    def create_user_role_table(self):
        query = f"""
        CREATE TABLE IF NOT EXISTS user_role (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL REFERENCES users(id),
            user_type VARCHAR(250) NOT NULL CHECK (user_type IN  {tuple(ALLOWED_ROLES)})
        );
        """
        self.db.execute_query(query)


    def add_user_role(self, user_id, user_type):
        query = """
        INSERT INTO user_role (user_id, user_type)
        VALUES (%s, %s);
        """
        self.db.execute_query(query, (user_id, user_type))

    # def delete_user_role(self, user_id):
    #     query = "DELETE FROM users WHERE id = %s;"...........
    #     self.db.execute_query(query, (user_id,))
    