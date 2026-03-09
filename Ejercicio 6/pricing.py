from abc import ABC, abstractmethod


class PricingStrategy(ABC):
    """
    Interfaz para las estrategias de cálculo de precio.
    """

    @abstractmethod
    def calculate_price(self, base_price: float) -> float:
        """
        Calcula el precio final a partir de un precio base.
        """
        pass



class EconomyPricing(PricingStrategy):
    """
    Estrategia de precio para clase económica.
    """

    def calculate_price(self, base_price: float) -> float:
        """
        Retorna el precio base sin incremento.
        """
        return base_price
    


class PremiumPricing(PricingStrategy):
    """
    Estrategia de precio para clase premium.
    """

    def calculate_price(self, base_price: float) -> float:
        """
        Retorna el precio base con un incremento del 30%.
        """
        return base_price * 1.30