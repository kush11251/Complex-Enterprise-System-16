from fastapi import APIRouter
from src.services import user_service

user_router = APIRouter()

@user_router.get('/users/')
def read_users():
    return user_service.get_users()