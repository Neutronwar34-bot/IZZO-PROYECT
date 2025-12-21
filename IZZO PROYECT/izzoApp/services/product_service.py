from izzoApp.repositories.product_repo import ProductRepository


class ProductService:

    @staticmethod
    def list_products():
        return ProductRepository.get_all()

    @staticmethod
    def get_product(product_id: int):
        product = ProductRepository.get_by_id(product_id)
        if not product or not product.is_active:
            raise ValueError("Product not found")
        return product

    @staticmethod
    def create_product(data: dict):
        if ProductRepository.get_by_sku(data["sku"]):
            raise ValueError("SKU already exists")

        return ProductRepository.create(data)

    @staticmethod
    def update_product(product_id: int, data: dict):
        product = ProductRepository.get_by_id(product_id)
        if not product:
            raise ValueError("Product not found")

        return ProductRepository.update(product, data)

    @staticmethod
    def delete_product(product_id: int):
        product = ProductRepository.get_by_id(product_id)
        if not product:
            raise ValueError("Product not found")

        ProductRepository.deactivate(product)
