from app.infrastructure.db_connection import Database

# from config.config import ALLOWED_ROLES, USER_ROLE_FIELDS


class UserOtpRepository:
    def __init__(self):
        self.db = Database()


    def create_user_otp_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS user_otp (
            user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            otp VARCHAR(50) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (user_id, otp)
        );
        """
        self.db.execute_query(query)

    
    # def insert_user_otp(self, user_id, otp):
    #     query = """
    #     INSERT INTO user_otp (user_id, otp)
    #     VALUES (%s, %s);
    #     """
    #     self.db.execute_query(query, (user_id, otp))

    
    # def validate_otp(self, user_id, otp):
    #     query = """
    #     SELECT COUNT(*)
    #     FROM user_otp
    #     WHERE user_id = %s AND otp = %s AND created_at >= NOW() - INTERVAL '5 minutes';
    #     """
    #     # result = self.db.fetch_one(query, (user_id, otp))
    #     return result[0] > 0

