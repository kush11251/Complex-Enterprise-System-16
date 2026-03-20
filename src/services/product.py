from src.models import Product
from src.repositories import product_repository

class ProductService:
    def get_products(self):
        return product_repository.get_products()

product_service = ProductService()