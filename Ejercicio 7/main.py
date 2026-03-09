"""
Script principal del Sistema de Inventario Inteligente.

Demuestra el uso de múltiples patrones de diseño:
- Singleton: InventoryConfig
- Factory: ProductFactory
- Observer: InventoryManager con EmailAlert y SMSAlert
- Strategy: Estrategias de reposición (Fixed, DemandBased, Seasonal)
- Adapter: SupplierAdapter
- Repository: ProductRepository
- Facade: InventoryFacade
"""

from inventory_facade import InventoryFacade
from strategy import DemandBasedReorderStrategy


def main():
    """
    Función principal que ejecuta la demostración del sistema.
    """
    print("\n=== SISTEMA DE INVENTARIO INTELIGENTE ===\n")
    
    # Crear la fachada del sistema
    inventory = InventoryFacade()
    
    # Registrar productos de diferentes tipos
    inventory.register_product("electronics", "Laptop", 5)
    inventory.register_product("food", "Manzanas", 50)
    inventory.register_product("clothing", "Camiseta", 8)
    
    print("\n--- Monitoreo de inventario ---\n")
    
    # Monitorear productos
    inventory.monitor_inventory("Laptop")
    inventory.monitor_inventory("Manzanas")
    inventory.monitor_inventory("Camiseta")
    
    print("\n--- Cambiando estrategia de reposición ---\n")
    
    # Cambiar a estrategia basada en demanda
    inventory.change_strategy(DemandBasedReorderStrategy())
    
    # Monitorear nuevamente con la nueva estrategia
    inventory.monitor_inventory("Laptop")


if __name__ == "__main__":
    main()
