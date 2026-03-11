# =========================================================
# ADAPTER - PROVEEDOR EXTERNO
# =========================================================

class ExternalSupplierAPI:

    def place_order(self, product_name, quantity):
        print(f"[Proveedor Externo] Orden recibida: {product_name} x{quantity}")


class SupplierAdapter:

    def __init__(self, external_api):
        self.external_api = external_api

    def order_product(self, product_name, quantity):

        self.external_api.place_order(product_name, quantity)
