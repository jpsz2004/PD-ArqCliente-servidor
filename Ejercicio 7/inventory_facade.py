"""
Módulo del patrón Facade para el sistema de inventario.

Proporciona una interfaz simplificada para interactuar
con todos los subsistemas del inventario.
"""

from models import InventoryConfig, ProductFactory, ProductRepository
from observer import InventoryManager, EmailAlert, SMSAlert
from strategy import FixedReorderStrategy, ReorderStrategy
from adapter import ExternalSupplierAPI, SupplierAdapter


class InventoryFacade:
    """
    Fachada principal del sistema de inventario.
    
    Integra todos los patrones y subsistemas, proporcionando
    una interfaz simple y unificada para gestionar el inventario.
    """
    
    def __init__(self):
        """
        Inicializa la fachada y configura todos los subsistemas.
        """
        # Repository para almacenamiento
        self.repository = ProductRepository()
        
        # Observer para notificaciones
        self.manager = InventoryManager()
        
        # Strategy por defecto
        self.strategy = FixedReorderStrategy()
        
        # Suscribir observadores
        self.manager.subscribe(EmailAlert())
        self.manager.subscribe(SMSAlert())
        
        # Adapter para proveedor externo
        supplier_api = ExternalSupplierAPI()
        self.supplier = SupplierAdapter(supplier_api)
    
    def register_product(self, product_type: str, name: str, stock: int) -> None:
        """
        Registra un nuevo producto en el inventario.
        
        Args:
            product_type (str): Tipo de producto ('electronics', 'food', 'clothing').
            name (str): Nombre del producto.
            stock (int): Cantidad inicial en stock.
        """
        product = ProductFactory.create_product(product_type, name, stock)
        self.repository.add(product)
        print(f"Producto registrado: {product}")
    
    def monitor_inventory(self, product_name: str) -> None:
        """
        Monitorea el inventario de un producto y toma acciones si es necesario.
        
        Verifica el stock contra el umbral configurado. Si está bajo,
        notifica a los observadores, ejecuta la estrategia de reposición
        y ordena al proveedor.
        
        Args:
            product_name (str): Nombre del producto a monitorear.
        """
        config = InventoryConfig()
        product = self.repository.get(product_name)
        
        if not product:
            print("Producto no encontrado")
            return
        
        print(f"Revisando inventario de {product}")
        
        if product.stock < config.get_min_stock_threshold():
            # Stock bajo detectado
            message = f"Stock bajo detectado en {product.name}"
            self.manager.notify(message)
            
            # Ejecutar estrategia de reposición
            self.strategy.reorder(product)
            
            # Ordenar al proveedor
            self.supplier.order_product(product.name, 20)
        else:
            print("Stock suficiente")
    
    def change_strategy(self, strategy: ReorderStrategy) -> None:
        """
        Cambia la estrategia de reposición actual.
        
        Args:
            strategy (ReorderStrategy): Nueva estrategia a utilizar.
        """
        self.strategy = strategy
        print("Estrategia de reposición actualizada")
