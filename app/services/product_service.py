from app.repositories.product_repository import ProductRepository

class ProductService:
    @staticmethod
    def list_products():
        products = ProductRepository.get_all_products()
        return [{'id': product.id, 'name': product.name, 'stock': product.stock, 'price': product.price} for product in products]

    @staticmethod
    def add_product(data):
        return ProductRepository.create_product(data)
