from inventory_facade import InventoryFacade
from strategy import DemandBasedReorderStrategy

# =========================================================
# DEMO DEL SISTEMA
# =========================================================

def main():

    print("\n=== SISTEMA DE INVENTARIO INTELIGENTE ===\n")

    inventory = InventoryFacade()

    # Registrar productos
    inventory.register_product("electronics", "Laptop", 5)
    inventory.register_product("food", "Manzanas", 50)
    inventory.register_product("clothing", "Camiseta", 8)

    print("\n--- Monitoreo de inventario ---\n")

    inventory.monitor_inventory("Laptop")
    inventory.monitor_inventory("Manzanas")
    inventory.monitor_inventory("Camiseta")

    print("\n--- Cambiando estrategia de reposición ---\n")

    inventory.change_strategy(DemandBasedReorderStrategy())

    inventory.monitor_inventory("Laptop")


if __name__ == "__main__":
    main()
