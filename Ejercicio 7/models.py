# =========================================================
# SINGLETON - CONFIGURACIÓN GLOBAL DEL INVENTARIO
# =========================================================

class InventoryConfig:

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.min_stock_threshold = 10

        return cls._instance


# =========================================================
# PRODUCTOS
# =========================================================

class Product:

    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def __str__(self):
        return f"{self.name} (Stock: {self.stock})"


class ElectronicProduct(Product):
    pass


class FoodProduct(Product):
    pass


class ClothingProduct(Product):
    pass


# =========================================================
# FACTORY - CREACIÓN DE PRODUCTOS
# =========================================================

class ProductFactory:

    @staticmethod
    def create_product(product_type, name, stock):

        if product_type == "electronics":
            return ElectronicProduct(name, stock)

        elif product_type == "food":
            return FoodProduct(name, stock)

        elif product_type == "clothing":
            return ClothingProduct(name, stock)

        else:
            raise ValueError("Tipo de producto no soportado")


# =========================================================
# REPOSITORY - ALMACENAMIENTO DE PRODUCTOS
# =========================================================

class ProductRepository:

    def __init__(self):
        self.products = {}

    def add(self, product):

        self.products[product.name] = product

    def get(self, name):

        return self.products.get(name)

    def update_stock(self, name, stock):

        if name in self.products:
            self.products[name].stock = stock

    def list_products(self):

        return self.products.values()
