from src.models import User
from src.repositories import user_repository

class UserService:
    def get_users(self):
        return user_repository.get_users()

user_service = UserService()