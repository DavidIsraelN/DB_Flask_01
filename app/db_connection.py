import os
import psycopg2 # type: ignore
# from dotenv import load_dotenv

# load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")


class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None


    def connect(self):
        """
        Creates a connection to the PostgreSQL database using environment variables.
        Returns a connection object.
        """
        try:
            self.conn = psycopg2.connect(
                host=DB_HOST,
                port=DB_PORT,
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )
            self.cursor = self.conn.cursor()
            print("Connected to the database successfully.")
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            raise


    def execute_query(self, query, params=None):
        """
        connects to the database if not already connected,
        executes a query with optional parameters and returns results if applicable.
        """
        try:
            if not self.conn or self.conn.closed:
                self.connect()
            self.cursor.execute(query, params)
            self.conn.commit()
            
            if query.strip().upper().startswith("SELECT") or "RETURNING" in query.strip().upper():
                return self.cursor.fetchall()
        
        except Exception as e:
            print(f"Error executing query: {e}")
            self.conn.rollback()
            raise

        finally:
            self.close()  # close the connection after executing the query


    def close(self):
        """
        Closes the database connection.
        """
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("Database connection closed.")


    # def execute_query(self, query, params=None):
    #     """
    #     Executes a query and returns results if applicable.
    #     """
    #     try:
    #         self.cursor.execute(query, params)
    #         if query.strip().upper().startswith("SELECT"):
    #             return self.cursor.fetchall()
    #         self.conn.commit()
    #     except Exception as e:
    #         print(f"Error executing query: {e}")
    #         self.conn.rollback()
    #         raise



# # Singleton pattern to ensure only one instance of the database connection exists
# import threading


# class Database:
#     _instance = None
#     _lock = threading.Lock()

#     def __new__(cls, *args, **kwargs):
#         """מבטיח מופע יחיד של המחלקה (Singleton)."""
#         if not cls._instance:
#             with cls._lock:
#                 if not cls._instance:
#                     cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
#                     cls._instance._initialize()
#         return cls._instance

#     def _initialize(self):
#         """אתחול המחלקה - חיבור למסד הנתונים."""
#         self.conn = None
#         self.cursor = None
#         self.connect()

#     def connect(self):
#         """יוצר חיבור למסד הנתונים אם לא קיים."""
#         if not self.conn:
#             try:
#                 self.conn = psycopg2.connect(
#                     database=os.getenv("POSTGRES_DB", "mydb"),
#                     user=os.getenv("POSTGRES_USER", "myuser"),
#                     password=os.getenv("POSTGRES_PASSWORD", "secret"),
#                     host=os.getenv("DB_HOST", "localhost"),
#                     port=os.getenv("DB_PORT", "5432"),
#                     cursor_factory=RealDictCursor
#                 )
#                 self.cursor = self.conn.cursor()
#                 print("Connected to the database successfully.")
#             except Exception as e:
#                 print(f"Error connecting to the database: {e}")
#                 raise

#     def execute_query(self, query, params=None):
#         """מבצע שאילתה ומחזיר תוצאות (אם יש)."""
#         try:
#             self.cursor.execute(query, params)
#             if query.strip().upper().startswith("SELECT"):
#                 return self.cursor.fetchall()
#             self.conn.commit()
#         except Exception as e:
#             print(f"Error executing query: {e}")
#             self.conn.rollback()
#             raise

#     def close(self):
#         """סוגר את החיבור למסד הנתונים."""
#         if self.cursor:
#             self.cursor.close()
#             self.cursor = None
#         if self.conn:
#             self.conn.close()
#             self.conn = None
#             print("Database connection closed.")





# def get_db_connection():
#     """
#     Creates a connection to the PostgreSQL database using environment variables.
#     Returns a connection object.
#     """
#     try:
#         conn = psycopg2.connect(
#             host=DB_HOST,
#             port=DB_PORT,
#             dbname=DB_NAME,
#             user=DB_USER,
#             password=DB_PASSWORD,
#         )
#         return conn
#     except Exception as e:
#         print(f"Error connecting to the database: {e}")
#         raise