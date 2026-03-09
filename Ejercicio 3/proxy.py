"""
Módulo del patrón Proxy para control de acceso.

Implementa el patrón Proxy para controlar el acceso
a operaciones sensibles basándose en roles de usuario.
"""

from models import User


class GradeService:
    """
    Servicio real para asignar calificaciones.
    
    Realiza la operación efectiva de asignación de notas.
    """
    
    def assign_grade(self, student_name: str, grade: int) -> None:
        """
        Asigna una calificación a un estudiante.
        
        Args:
            student_name (str): Nombre del estudiante.
            grade (int): Calificación a asignar.
        """
        print(f"Nota {grade} asignada a {student_name}")


class GradeServiceProxy:
    """
    Proxy que controla el acceso al servicio de calificaciones.
    
    Implementa el patrón Proxy para verificar permisos
    antes de permitir la asignación de calificaciones.
    Solo los profesores pueden asignar notas.
    """
    
    def __init__(self, user: User):
        """
        Inicializa el proxy con un usuario.
        
        Args:
            user (User): Usuario que intenta realizar la operación.
        """
        self.user = user
        self.service = GradeService()
    
    def assign_grade(self, student_name: str, grade: int) -> None:
        """
        Intenta asignar una calificación verificando permisos primero.
        
        Solo permite la operación si el usuario es un profesor.
        
        Args:
            student_name (str): Nombre del estudiante.
            grade (int): Calificación a asignar.
        """
        if self.user.role != "professor":
            print("Acceso denegado: solo los profesores pueden asignar notas")
            return
        
        self.service.assign_grade(student_name, grade)
