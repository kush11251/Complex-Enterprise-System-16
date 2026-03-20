from fastapi import APIRouter
from src.services import product_service

product_router = APIRouter()

@product_router.get('/products/')
def read_products():
    return product_service.get_products()