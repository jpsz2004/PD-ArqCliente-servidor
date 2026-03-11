from abc import ABC, abstractmethod

# =========================================================
# STRATEGY - ESTRATEGIAS DE REPOSICIÓN
# =========================================================

class ReorderStrategy(ABC):

    @abstractmethod
    def reorder(self, product):
        pass


class FixedReorderStrategy(ReorderStrategy):

    def reorder(self, product):
        print(f"Reposición fija para {product.name}: ordenando 20 unidades")


class DemandBasedReorderStrategy(ReorderStrategy):

    def reorder(self, product):
        print(f"Reposición basada en demanda para {product.name}")


class SeasonalReorderStrategy(ReorderStrategy):

    def reorder(self, product):
        print(f"Reposición estacional para {product.name}")
