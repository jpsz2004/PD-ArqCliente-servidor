from abc import ABC, abstractmethod

# =========================================================
# STRATEGY PATTERN
# Generación de reportes
# =========================================================

class ReportStrategy(ABC):

    @abstractmethod
    def generate(self, data):
        pass


class PDFReportStrategy(ReportStrategy):

    def generate(self, data):
        print("\n--- Reporte PDF ---")
        for student, grade in data.items():
            print(f"{student}: {grade}")


class CSVReportStrategy(ReportStrategy):

    def generate(self, data):
        print("\n--- Reporte CSV ---")
        print("Estudiante,Nota")
        for student, grade in data.items():
            print(f"{student},{grade}")


class JSONReportStrategy(ReportStrategy):

    def generate(self, data):
        import json
        print("\n--- Reporte JSON ---")
        print(json.dumps(data, indent=4))


class ReportGenerator:

    def __init__(self, strategy):
        self.strategy = strategy

    def generate_report(self, data):
        self.strategy.generate(data)
