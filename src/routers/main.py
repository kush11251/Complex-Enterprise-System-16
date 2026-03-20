from fastapi import APIRouter
from src.controllers import user_controller, product_controller

main_router = APIRouter()
main_router.include_router(user_controller.router)
main_router.include_router(product_controller.router)