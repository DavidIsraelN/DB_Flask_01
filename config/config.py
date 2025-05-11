# Configuration constants 

BASE_API_URL = "https://api.nobelprize.org/v1/" 
URL_COUNTRY = BASE_API_URL + "country.json"

# USER_FIELDS: List of required data fields for user table 
USER_FIELDS = ["first_name", "last_name", "country", "national_id", "phone_number"]

# USER_ROLE_FIELDS: List of required data fields for user role table 
USER_ROLE_FIELDS = ["user_id", "user_type"]

# USER_OTP_FIELDS: List of required data fields for user otp table 
USER_ROLE_FIELDS = ["user_id", "otp"]

# ALLOWED_ROLES: List of valid user 'role types' in the role table
ALLOWED_ROLES = ["admin", "teacher", "student"]
