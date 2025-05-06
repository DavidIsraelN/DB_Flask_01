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


    def add_user(self, data):
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        country = data.get('country')
        national_id = data.get('national_id')
        phone_number = data.get('phone_number')

        if not first_name or not last_name or not country or not national_id or not phone_number:
            raise ValueError("All fields are required")
                
        return self.user_repo.add_user(first_name, last_name, country, national_id, phone_number)


    # def get_user_by_id(self, user_id):
    #     user = self.user_repo.get_user_by_id(user_id)
    #     if not user:
    #         raise ValueError("User not found")
    #     return user


    # def delete_user(self, user_id):
    #     user = self.user_repo.get_user_by_id(user_id)
    #     if not user:
    #         raise ValueError("User not found")
    #     self.user_repo.delete_user(user_id)
