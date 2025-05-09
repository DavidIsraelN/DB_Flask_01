# Configuration constants 

# USER_FIELDS: List of required data fields for user table 
USER_FIELDS = ["first_name", "last_name", "country", "national_id", "phone_number"]

# USER_ROLE_FIELDS: List of required data fields for user role table 
USER_ROLE_FIELDS = ["user_id", "user_type"]

# ALLOWED_ROLES: List of valid user 'role types' in the role table
ALLOWED_ROLES = ["admin", "teacher", "student"]
