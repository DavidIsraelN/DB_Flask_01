from .user_repository import UserRepository


class UserService:
    def __init__(self):
        self.user_repo = UserRepository()


    def create_user_table(self):
        self.user_repo.create_user_table()

    
    def create_user_role_table(self):
        self.user_repo.create_user_role_table()


    def get_all_users(self):
        return self.user_repo.get_all_users()
        # we can add business logic here if needed like terurn all users sorting by last name and first_name
        # return sorted(self.user_repo.get_all_users(), key=lambda user: (user['last_name'], user['first_name']))


    def get_user_by_id(self, user_id):
        user = self.user_repo.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return user


    def add_user(self, data):
        self.check_user_data(data)
        new_item_id = self.user_repo.add_user(data.get('first_name'), data.get('last_name'), data.get('country'), 
                                              data.get('national_id'), data.get('phone_number'))
        if not new_item_id:
            raise ValueError("Failed to add user")
        
        return self.get_user_by_id(str(new_item_id))
        # return {
        #     'id': new_item_id,
        #     'first_name': first_name,
        #     'last_name': last_name,
        #     'country': country,
        #     'national_id': national_id,
        #     'phone_number': phone_number
        # }


    def add_user_with_role(self, data):
        """
        Add a new user with a specific role.
        :param data: Dictionary containing user data and role.
        where user is a dictionary containing user data (first_name, last_name, country, national_id, phone_number), 
        and role is a string representing the user role (student, teacher, admin).
        :return: Dictionary containing the new user and their role.
        """
        self.check_user_with_role_data(data)
        user_data = data.get('user')
        new_item_id = self.user_repo.add_user(user_data.get('first_name'), user_data.get('last_name'), user_data.get('country'),
                                              user_data.get('national_id'), user_data.get('phone_number'))
        if not new_item_id:
            raise ValueError("Failed to add user")
        
        # print(f"new_user (type {type(new_user)}) is: { new_user }")

        user_role = data.get('role')
        self.user_repo.add_user_role(new_item_id, user_role)

        return {
            "user": self.get_user_by_id(str(new_item_id)),
            "role": user_role
        }


    def check_user_data(self, data):
        required_fields = ['first_name', 'last_name', 'country', 'national_id', 'phone_number']
        for field in required_fields:
            if field not in data:
                raise ValueError("All fields of user are required")


    def check_user_with_role_data(self, data):
        for field in ['user', 'role']:
            if field not in data:
                raise ValueError("User data and role are required")
        self.check_user_data(data.get('user'))
        if data.get('role') not in ['student', 'teacher', 'admin']:
            raise ValueError("Invalid role. Must be 'student', 'teacher', or 'admin'")


    # def delete_user(self, user_id):
    #     user = self.user_repo.get_user_by_id(user_id)
    #     if not user:
    #         raise ValueError("User not found")
    #     self.user_repo.delete_user(user_id)
