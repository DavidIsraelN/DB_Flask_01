from app.infrastructure.db_connection import Database

from config.config import ALLOWED_ROLES, USER_ROLE_FIELDS


class UserRoleRepository:
    def __init__(self):
        self.db = Database()
    

    def create_user_role_table(self):
        query = f"""
        CREATE TABLE IF NOT EXISTS user_role (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL REFERENCES users(id) UNIQUE,
            user_type VARCHAR(250) NOT NULL CHECK (user_type IN  {tuple(ALLOWED_ROLES)})
        );
        """
        self.db.execute_query(query)


    def add_user_role(self, user_id, user_type):
        placeholders = ', '.join(['%s'] * len(USER_ROLE_FIELDS))
        query = f"""
        INSERT INTO user_role ({', '.join(USER_ROLE_FIELDS)})
        VALUES ({placeholders});
        """
        self.db.execute_query(query, (user_id, user_type))
    

    def update_user_role(self, user_id, user_type):
        """
        Update the role of a user in the database.
        :param user_id: ID of the user to update.
        :param role: The new role to assign to the user.
        """
        placeholders = ', '.join(['%s'] * len(USER_ROLE_FIELDS))
        query = f"""
        INSERT INTO user_role ({', '.join(USER_ROLE_FIELDS)})
        VALUES ({placeholders})
        ON CONFLICT (user_id) DO UPDATE SET user_type = EXCLUDED.user_type;
        """
        self.db.execute_query(query, (user_id, user_type))


    # def delete_user_role(self, user_id):
    #     query = "DELETE FROM users WHERE id = %s;"...........
    #     self.db.execute_query(query, (user_id,))
    