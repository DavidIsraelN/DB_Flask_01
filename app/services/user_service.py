from repositories.user_role_repository import UserRoleRepository
from repositories.user_repository import UserRepository
from .nobel_service import NobelService
from config.config import USER_FIELDS, ALLOWED_ROLES


nobel_service = NobelService()

class UserService:
    def __init__(self):
        self.user_repo = UserRepository()
        self.user_role_repo = UserRoleRepository()


    def create_user_table(self):
        self.user_repo.create_user_table()

    
    def create_user_role_table(self):
        self.user_role_repo.create_user_role_table()


    def get_all_users(self):                          # make it dict!!
        return self.user_repo.get_all_users()
        # we can add business logic here if needed like terurn all users sorting by last name and first_name
        # return sorted(self.user_repo.get_all_users(), key=lambda user: (user['last_name'], user['first_name']))


    def get_user_by_id(self, user_id):
        user = self.user_repo.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return self.build_user_dict(["id"] + USER_FIELDS, list(user[0]))


    def get_user_with_role(self, user_id):
        if not user_id:
            raise ValueError("User ID is required")

        user_values = self.user_repo.get_user_with_role_by_id(user_id)
        if not user_values:
            raise ValueError(f"User with ID {user_id} not found")
        
        values = list(user_values[0])
        values[-1] = values[-1] if values[-1] else "No role assigned"
        
        return self.build_user_dict(["id"] + USER_FIELDS + ["role"], values)
    

    def get_country_code(self, user_id):
        if not user_id:
            raise ValueError("User ID is required")

        country = self.user_repo.get_country_by_user_id(user_id)
        if not country:
            raise ValueError(f"Country not found for user ID {user_id}. user may not exist.")

        return {"user_id": user_id, "country_code": nobel_service.get_country_code(country[0][0])}


    def add_user(self, data):
        self.check_user_data(data)
        user_data = {field: data.get(field) for field in USER_FIELDS}

        new_item_id = self.user_repo.add_user(**user_data)
        if not new_item_id:
            raise ValueError("Failed to add user")

        return self.build_user_dict(["id"] + USER_FIELDS, [new_item_id] + list(user_data.values()))        
        # return {'id': new_item_id, **user_data}
        # return self.get_user_by_id(str(new_item_id))


    def add_user_with_role(self, data):
        """
        Add a new user with a specific role.
        :param data: Dictionary containing user data and role.
        where user is a dictionary containing user data (first_name, last_name, country, national_id, phone_number), 
        and role is a string representing the user role (student, teacher, admin).
        :return: Dictionary containing the new user and their role.
        """
        self.check_user_with_role_data(data)
        user_values = data.get('user')
        user_data = {field: user_values.get(field) for field in USER_FIELDS}

        new_item_id = self.user_repo.add_user(**user_data)
        if not new_item_id:
            raise ValueError("Failed to add user")
        
        user_role = data.get('role')
        self.user_role_repo.add_user_role(new_item_id, user_role)

        return self.build_user_dict(["id"] + USER_FIELDS + ["role"], [new_item_id] + list(user_data.values()) + [user_role])
        # return {'id': new_item_id, **user_data, 'role': user_role}
        # return {"user": self.get_user_by_id(str(new_item_id)),"role": user_role}


    # def update_user(self, user_id, data):
    #     """
    #     Update user details in the database.
    #     :param user_id: ID of the user to update.
    #     :param data: Dictionary containing the fields to update and their new values.
    #     """
    #     print(f"in update: {data.items()}")
    #     user_updates = {key: value for key, value in data.items() if key in USER_FIELDS}

    #     print(user_updates)
    #     if not user_updates:
    #         raise ValueError("No valid fields provided for update.")
    #
    #     self.user_repo.update_user(user_id, updates)


    def update_user(self, user_id, data):
        """
        Update user details and role in the database.
        :param user_id: ID of the user to update.
        :param data: Dictionary containing the fields to update and their new values.
        """
        if not user_id:
            raise ValueError("User ID is required")
        
        user_updates = {key: value for key, value in data.items() if key in USER_FIELDS}
        role_updates = data.get("role")

        if not user_updates and not role_updates:
            raise ValueError("No valid fields or role provided for update.")
        
        if role_updates:
            self.check_role_data(role_updates)
            self.user_role_repo.update_user_role(user_id, role_updates)

        if user_updates:
            self.user_repo.update_user(user_id, user_updates)

        return self.get_user_with_role(user_id)


    def check_user_data(self, data):
        for field in USER_FIELDS:
            if field not in data:
                raise ValueError("All fields of user are required")


    def check_role_data(self, role):
        if role not in ALLOWED_ROLES:
            raise ValueError("Invalid role. Must be 'student', 'teacher', or 'admin'")


    def check_user_with_role_data(self, data):
        for field in ['user', 'role']:
            if field not in data:
                raise ValueError("User data and role are required")
        self.check_user_data(data.get('user'))
        self.check_role_data(data.get('role'))


    def build_user_dict(self, keys, user_values):
        return dict(zip(keys, user_values))

    
    # def delete_user(self, user_id):
    #     user = self.user_repo.get_user_by_id(user_id)
    #     if not user:
    #         raise ValueError("User not found")
    #     self.user_repo.delete_user(user_id)
