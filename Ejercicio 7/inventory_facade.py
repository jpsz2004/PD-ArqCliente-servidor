from models import InventoryConfig, ProductFactory, ProductRepository
from observer import InventoryManager, EmailAlert, SMSAlert
from strategy import FixedReorderStrategy
from adapter import ExternalSupplierAPI, SupplierAdapter

# =========================================================
# FACADE - INTERFAZ SIMPLIFICADA DEL INVENTARIO
# =========================================================

class InventoryFacade:

    def __init__(self):

        self.repository = ProductRepository()
        self.manager = InventoryManager()

        self.strategy = FixedReorderStrategy()

        # Observadores
        self.manager.subscribe(EmailAlert())
        self.manager.subscribe(SMSAlert())

        # Adapter proveedor
        supplier_api = ExternalSupplierAPI()
        self.supplier = SupplierAdapter(supplier_api)

    # Registrar producto
    def register_product(self, product_type, name, stock):

        product = ProductFactory.create_product(product_type, name, stock)

        self.repository.add(product)

        print(f"Producto registrado: {product}")

    # Monitorear inventario
    def monitor_inventory(self, product_name):

        config = InventoryConfig()

        product = self.repository.get(product_name)

        if not product:
            print("Producto no encontrado")
            return

        print(f"Revisando inventario de {product}")

        if product.stock < config.min_stock_threshold:

            message = f"Stock bajo detectado en {product.name}"

            self.manager.notify(message)

            # Estrategia de reposición
            self.strategy.reorder(product)

            # Orden al proveedor
            self.supplier.order_product(product.name, 20)

        else:

            print("Stock suficiente")

    # Cambiar estrategia
    def change_strategy(self, strategy):

        self.strategy = strategy
        print("Estrategia de reposición actualizada")
