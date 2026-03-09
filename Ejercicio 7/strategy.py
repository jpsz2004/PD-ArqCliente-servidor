"""
Módulo del patrón Strategy para estrategias de reposición.

Implementa diferentes estrategias de reposición de inventario
que pueden ser intercambiadas dinámicamente.
"""

from abc import ABC, abstractmethod
from models import Product


class ReorderStrategy(ABC):
    """
    Interfaz abstracta para las estrategias de reposición.
    
    Define el contrato que deben seguir todas las estrategias
    concretas de reposición.
    """
    
    @abstractmethod
    def reorder(self, product: Product) -> None:
        """
        Ejecuta la estrategia de reposición para un producto.
        
        Args:
            product (Product): Producto que necesita reposición.
        """
        pass


class FixedReorderStrategy(ReorderStrategy):
    """
    Estrategia de reposición con cantidad fija.
    
    Siempre ordena la misma cantidad de unidades,
    independientemente de la demanda.
    """
    
    def reorder(self, product: Product) -> None:
        """
        Ordena una cantidad fija de 20 unidades.
        
        Args:
            product (Product): Producto a reponer.
        """
        print(f"Reposición fija para {product.name}: ordenando 20 unidades")


class DemandBasedReorderStrategy(ReorderStrategy):
    """
    Estrategia de reposición basada en la demanda.
    
    Calcula la cantidad a ordenar según patrones de demanda
    históricos.
    """
    
    def reorder(self, product: Product) -> None:
        """
        Ordena basándose en análisis de demanda.
        
        Args:
            product (Product): Producto a reponer.
        """
        print(f"Reposición basada en demanda para {product.name}")


class SeasonalReorderStrategy(ReorderStrategy):
    """
    Estrategia de reposición estacional.
    
    Ajusta las cantidades según la temporada del año
    y eventos especiales.
    """
    
    def reorder(self, product: Product) -> None:
        """
        Ordena considerando la temporada actual.
        
        Args:
            product (Product): Producto a reponer.
        """
        print(f"Reposición estacional para {product.name}")
