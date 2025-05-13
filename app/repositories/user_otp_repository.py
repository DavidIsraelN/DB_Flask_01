from app.infrastructure.db_connection import Database

from config.config import USER_OTP_FIELDS


class UserOtpRepository:
    def __init__(self):
        self.db = Database()


    def create_user_otp_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS user_otp (
            user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            otp VARCHAR(10) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (user_id, otp),
            UNIQUE (user_id)
        );
        """
        self.db.execute_query(query)


    def add_user_otp(self, user_id, otp):
        """
        Inserts or updates the OTP for a user.
        """
        placeholders = ', '.join(['%s'] * len(USER_OTP_FIELDS))
        query = f"""
           INSERT INTO user_otp ({', '.join(USER_OTP_FIELDS)})
           VALUES ({placeholders})
           ON CONFLICT (user_id) DO UPDATE
             SET otp = EXCLUDED.otp,
                 created_at = CURRENT_TIMESTAMP;
           """
        self.db.execute_query(query, (user_id, otp))

    
    # def validate_otp(self, user_id, otp):
    #     query = """
    #     SELECT COUNT(*)
    #     FROM user_otp
    #     WHERE user_id = %s AND otp = %s AND created_at >= NOW() - INTERVAL '5 minutes';
    #     """
    #     result = self.db.fetch_one(query, (user_id, otp))
    #     return result[0] > 0


    def validate_otp(self, user_id, otp, window_minutes=5):
        """
        Returns True if OTP matches and is within the time window.
        """
        query = """
        SELECT COUNT(*)
        FROM user_otp
        WHERE user_id = %s
          AND otp = %s
          AND created_at >= NOW() - INTERVAL '%s minutes';
        """
        result = self.db.execute_query(query, (user_id, otp, window_minutes))
        return result and result[0][0] > 0
