from src.models import Product

class ProductRepository:
    def get_products(self):
        # Mock data
        return [Product(id=1, name='Product A'), Product(id=2, name='Product B')]

product_repository = ProductRepository()