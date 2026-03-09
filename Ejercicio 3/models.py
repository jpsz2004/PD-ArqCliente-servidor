"""
Módulo de modelos y patrones estructurales del sistema LMS.

Contiene:
- Clases de usuario (User, Student, Professor, Admin)
- Clases de evaluación (Evaluation y sus subclases)
- Factory: EvaluationFactory
- Sistema LMS principal
"""

from abc import ABC, abstractmethod


# =========================================================
# USUARIOS DEL SISTEMA
# =========================================================

class User:
    """
    Clase base para representar un usuario del sistema LMS.
    
    Atributos:
        name (str): Nombre del usuario.
        role (str): Rol del usuario en el sistema.
    """
    
    def __init__(self, name: str, role: str):
        """
        Inicializa un usuario.
        
        Args:
            name (str): Nombre del usuario.
            role (str): Rol del usuario.
        """
        self.name = name
        self.role = role


class Student(User):
    """
    Usuario de tipo estudiante.
    """
    
    def __init__(self, name: str):
        """
        Inicializa un estudiante.
        
        Args:
            name (str): Nombre del estudiante.
        """
        super().__init__(name, "student")


class Professor(User):
    """
    Usuario de tipo profesor.
    """
    
    def __init__(self, name: str):
        """
        Inicializa un profesor.
        
        Args:
            name (str): Nombre del profesor.
        """
        super().__init__(name, "professor")


class Admin(User):
    """
    Usuario de tipo administrador.
    """
    
    def __init__(self, name: str):
        """
        Inicializa un administrador.
        
        Args:
            name (str): Nombre del administrador.
        """
        super().__init__(name, "admin")


# =========================================================
# EVALUACIONES
# =========================================================

class Evaluation(ABC):
    """
    Clase abstracta base para representar una evaluación.
    
    Atributos:
        title (str): Título de la evaluación.
        max_score (int): Puntaje máximo de la evaluación.
    """
    
    def __init__(self, title: str, max_score: int):
        """
        Inicializa una evaluación.
        
        Args:
            title (str): Título de la evaluación.
            max_score (int): Puntaje máximo.
        """
        self.title = title
        self.max_score = max_score
    
    @abstractmethod
    def evaluate(self, score: int) -> int:
        """
        Evalúa un puntaje.
        
        Args:
            score (int): Puntaje obtenido.
            
        Returns:
            int: Puntaje procesado.
        """
        pass


class QuizEvaluation(Evaluation):
    """
    Evaluación de tipo cuestionario.
    """
    
    def evaluate(self, score: int) -> int:
        """
        Evalúa un quiz.
        
        Args:
            score (int): Puntaje obtenido.
            
        Returns:
            int: Puntaje del quiz.
        """
        print(f"Evaluando Quiz '{self.title}': {score}/{self.max_score}")
        return score


class ProjectEvaluation(Evaluation):
    """
    Evaluación de tipo proyecto.
    """
    
    def evaluate(self, score: int) -> int:
        """
        Evalúa un proyecto.
        
        Args:
            score (int): Puntaje obtenido.
            
        Returns:
            int: Puntaje del proyecto.
        """
        print(f"Evaluando Proyecto '{self.title}': {score}/{self.max_score}")
        return score


class ExamEvaluation(Evaluation):
    """
    Evaluación de tipo examen.
    """
    
    def evaluate(self, score: int) -> int:
        """
        Evalúa un examen.
        
        Args:
            score (int): Puntaje obtenido.
            
        Returns:
            int: Puntaje del examen.
        """
        print(f"Evaluando Examen '{self.title}': {score}/{self.max_score}")
        return score


# =========================================================
# FACTORY - CREACIÓN DE EVALUACIONES
# =========================================================

class EvaluationFactory:
    """
    Patrón Factory para la creación de evaluaciones.
    
    Permite crear diferentes tipos de evaluaciones sin exponer
    la lógica de creación al cliente.
    """
    
    @staticmethod
    def create_evaluation(eval_type: str, title: str, max_score: int) -> Evaluation:
        """
        Crea una evaluación según el tipo especificado.
        
        Args:
            eval_type (str): Tipo de evaluación ('quiz', 'project', 'exam').
            title (str): Título de la evaluación.
            max_score (int): Puntaje máximo.
            
        Returns:
            Evaluation: Instancia de la evaluación creada.
            
        Raises:
            ValueError: Si el tipo de evaluación no es soportado.
        """
        if eval_type == "quiz":
            return QuizEvaluation(title, max_score)
        elif eval_type == "project":
            return ProjectEvaluation(title, max_score)
        elif eval_type == "exam":
            return ExamEvaluation(title, max_score)
        else:
            raise ValueError(f"Tipo de evaluación no soportado: {eval_type}")


# =========================================================
# SISTEMA LMS
# =========================================================

class LMS:
    """
    Sistema de gestión de aprendizaje (Learning Management System).
    
    Gestiona usuarios, cursos y calificaciones del sistema educativo.
    """
    
    def __init__(self):
        """
        Inicializa el sistema LMS con estructuras vacías.
        """
        self.users = []
        self.courses = []
        self.grades = {}
    
    def add_user(self, user: User) -> None:
        """
        Agrega un usuario al sistema.
        
        Args:
            user (User): Usuario a agregar.
        """
        self.users.append(user)
    
    def add_course(self, course) -> None:
        """
        Agrega un curso al sistema.
        
        Args:
            course: Curso a agregar.
        """
        self.courses.append(course)
    
    def save_grade(self, student_name: str, grade: int) -> None:
        """
        Guarda una calificación de un estudiante.
        
        Args:
            student_name (str): Nombre del estudiante.
            grade (int): Calificación obtenida.
        """
        self.grades[student_name] = grade
    
    def get_grades(self) -> dict:
        """
        Obtiene todas las calificaciones del sistema.
        
        Returns:
            dict: Diccionario con calificaciones por estudiante.
        """
        return self.grades
