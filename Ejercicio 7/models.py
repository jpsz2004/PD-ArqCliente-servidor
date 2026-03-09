"""
Módulo de modelos y patrones estructurales del sistema de inventario.

Contiene:
- Singleton: InventoryConfig
- Clases de producto
- Factory: ProductFactory
- Repository: ProductRepository
"""


class InventoryConfig:
    """
    Clase Singleton que centraliza la configuración del sistema de inventario.
    
    Garantiza que solo exista una única instancia de configuración
    durante toda la ejecución del programa.
    
    Atributos:
        min_stock_threshold (int): Umbral mínimo de stock para alertas.
    """
    
    _instance = None
    
    def __new__(cls):
        """
        Controla la creación de instancias para implementar el patrón Singleton.
        Si no existe una instancia, la crea. Si ya existe, devuelve la misma.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.min_stock_threshold = 10
        return cls._instance
    
    def get_min_stock_threshold(self) -> int:
        """Retorna el umbral mínimo de stock."""
        return self.min_stock_threshold
    
    def set_min_stock_threshold(self, value: int) -> None:
        """
        Actualiza el umbral mínimo de stock.
        
        Args:
            value (int): Nuevo valor del umbral.
        """
        self.min_stock_threshold = value


class Product:
    """
    Clase base para representar un producto en el inventario.
    
    Atributos:
        name (str): Nombre del producto.
        stock (int): Cantidad en stock.
    """
    
    def __init__(self, name: str, stock: int):
        """
        Inicializa un producto.
        
        Args:
            name (str): Nombre del producto.
            stock (int): Cantidad inicial en stock.
        """
        self.name = name
        self.stock = stock
    
    def __str__(self) -> str:
        """Retorna una representación legible del producto."""
        return f"{self.name} (Stock: {self.stock})"


class ElectronicProduct(Product):
    """Producto de tipo electrónico."""
    pass


class FoodProduct(Product):
    """Producto de tipo alimenticio."""
    pass


class ClothingProduct(Product):
    """Producto de tipo vestimenta."""
    pass


class ProductFactory:
    """
    Patrón Factory para la creación de productos.
    
    Permite crear diferentes tipos de productos sin exponer
    la lógica de creación al cliente.
    """
    
    @staticmethod
    def create_product(product_type: str, name: str, stock: int) -> Product:
        """
        Crea un producto según el tipo especificado.
        
        Args:
            product_type (str): Tipo de producto ('electronics', 'food', 'clothing').
            name (str): Nombre del producto.
            stock (int): Cantidad inicial en stock.
            
        Returns:
            Product: Instancia del producto creado.
            
        Raises:
            ValueError: Si el tipo de producto no es soportado.
        """
        if product_type == "electronics":
            return ElectronicProduct(name, stock)
        elif product_type == "food":
            return FoodProduct(name, stock)
        elif product_type == "clothing":
            return ClothingProduct(name, stock)
        else:
            raise ValueError(f"Tipo de producto no soportado: {product_type}")


class ProductRepository:
    """
    Patrón Repository para almacenamiento de productos.
    
    Proporciona una interfaz de abstracción para el almacenamiento
    y recuperación de productos.
    """
    
    def __init__(self):
        """Inicializa el repositorio con un diccionario vacío."""
        self.products = {}
    
    def add(self, product: Product) -> None:
        """
        Agrega un producto al repositorio.
        
        Args:
            product (Product): Producto a agregar.
        """
        self.products[product.name] = product
    
    def get(self, name: str) -> Product:
        """
        Obtiene un producto por su nombre.
        
        Args:
            name (str): Nombre del producto a buscar.
            
        Returns:
            Product: Producto encontrado o None si no existe.
        """
        return self.products.get(name)
    
    def update_stock(self, name: str, stock: int) -> None:
        """
        Actualiza el stock de un producto.
        
        Args:
            name (str): Nombre del producto.
            stock (int): Nuevo valor de stock.
        """
        if name in self.products:
            self.products[name].stock = stock
    
    def list_products(self):
        """
        Lista todos los productos en el repositorio.
        
        Returns:
            valores del diccionario de productos.
        """
        return self.products.values()
