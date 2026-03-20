from src.models import User

class UserRepository:
    def get_users(self):
        # Mock data
        return [User(id=1, name='John'), User(id=2, name='Jane')]

user_repository = UserRepository()