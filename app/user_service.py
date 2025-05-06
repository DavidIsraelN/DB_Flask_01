from .user_repository import UserRepository


class UserService:
    def __init__(self):
        self.user_repo = UserRepository()


    def get_all_users(self):
        return self.user_repo.get_all_users()
        # we can add business logic here if needed like terurn all users sorting by last name and first_name
        # return sorted(self.user_repo.get_all_users(), key=lambda user: (user['last_name'], user['first_name']))


    def add_user(self, data):
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email', "")  # Email is optional

        if not first_name or not last_name:
            raise ValueError('first name and last name are required')
        
        return self.user_repo.add_user(first_name, last_name, email)


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
