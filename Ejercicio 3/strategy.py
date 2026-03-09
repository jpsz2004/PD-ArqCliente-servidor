"""
Módulo del patrón Strategy para generación de reportes.

Implementa diferentes estrategias para generar reportes
en distintos formatos (PDF, CSV, JSON).
"""

from abc import ABC, abstractmethod


class ReportStrategy(ABC):
    """
    Interfaz abstracta para las estrategias de generación de reportes.
    
    Define el contrato que deben seguir todas las estrategias
    concretas de reportes.
    """
    
    @abstractmethod
    def generate(self, data: dict) -> None:
        """
        Genera un reporte con los datos proporcionados.
        
        Args:
            data (dict): Datos a incluir en el reporte.
        """
        pass


class PDFReportStrategy(ReportStrategy):
    """
    Estrategia para generar reportes en formato PDF.
    
    Simula la generación de un reporte en formato PDF.
    """
    
    def generate(self, data: dict) -> None:
        """
        Genera un reporte simulado en formato PDF.
        
        Args:
            data (dict): Diccionario con estudiantes y calificaciones.
        """
        print("\n--- Reporte PDF ---")
        for student, grade in data.items():
            print(f"{student}: {grade}")


class CSVReportStrategy(ReportStrategy):
    """
    Estrategia para generar reportes en formato CSV.
    
    Genera un reporte en formato de valores separados por comas.
    """
    
    def generate(self, data: dict) -> None:
        """
        Genera un reporte en formato CSV.
        
        Args:
            data (dict): Diccionario con estudiantes y calificaciones.
        """
        print("\n--- Reporte CSV ---")
        print("Estudiante,Nota")
        for student, grade in data.items():
            print(f"{student},{grade}")


class JSONReportStrategy(ReportStrategy):
    """
    Estrategia para generar reportes en formato JSON.
    
    Genera un reporte en formato JSON estructurado.
    """
    
    def generate(self, data: dict) -> None:
        """
        Genera un reporte en formato JSON.
        
        Args:
            data (dict): Diccionario con estudiantes y calificaciones.
        """
        import json
        print("\n--- Reporte JSON ---")
        print(json.dumps(data, indent=4))


class ReportGenerator:
    """
    Generador de reportes que utiliza una estrategia específica.
    
    Permite cambiar dinámicamente la estrategia de generación
    sin modificar el código cliente.
    """
    
    def __init__(self, strategy: ReportStrategy):
        """
        Inicializa el generador con una estrategia.
        
        Args:
            strategy (ReportStrategy): Estrategia de generación a usar.
        """
        self.strategy = strategy
    
    def generate_report(self, data: dict) -> None:
        """
        Genera un reporte usando la estrategia configurada.
        
        Args:
            data (dict): Datos a incluir en el reporte.
        """
        self.strategy.generate(data)
