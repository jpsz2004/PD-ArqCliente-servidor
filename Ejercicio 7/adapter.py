"""
Módulo del patrón Adapter para integración con proveedores externos.

Adapta la interfaz de sistemas externos de proveedores
al formato interno que utiliza el sistema de inventario.
"""


class ExternalSupplierAPI:
    """
    Simula una API externa de un proveedor.
    
    Esta API tiene su propia interfaz que puede ser
    incompatible con nuestro sistema interno.
    """
    
    def place_order(self, product_name: str, quantity: int) -> None:
        """
        Procesa una orden en el sistema externo del proveedor.
        
        Args:
            product_name (str): Nombre del producto a ordenar.
            quantity (int): Cantidad a ordenar.
        """
        print(f"[Proveedor Externo] Orden recibida: {product_name} x{quantity}")


class SupplierAdapter:
    """
    Adaptador que transforma las llamadas internas
    al formato esperado por la API externa del proveedor.
    
    Implementa el patrón Adapter para hacer compatible
    nuestro sistema con APIs externas.
    """
    
    def __init__(self, external_api: ExternalSupplierAPI):
        """
        Inicializa el adaptador con una instancia de la API externa.
        
        Args:
            external_api (ExternalSupplierAPI): API del proveedor externo.
        """
        self.external_api = external_api
    
    def order_product(self, product_name: str, quantity: int) -> None:
        """
        Ordena un producto adaptando la llamada al formato externo.
        
        Args:
            product_name (str): Nombre del producto.
            quantity (int): Cantidad a ordenar.
        """
        self.external_api.place_order(product_name, quantity)
