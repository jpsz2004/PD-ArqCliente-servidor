from abc import ABC, abstractmethod

# =========================================================
# USUARIOS DEL SISTEMA
# =========================================================

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


class Student(User):
    def __init__(self, name):
        super().__init__(name, "student")


class Professor(User):
    def __init__(self, name):
        super().__init__(name, "professor")


class Admin(User):
    def __init__(self, name):
        super().__init__(name, "admin")


# =========================================================
# FACTORY PATTERN
# Creación de evaluaciones
# =========================================================

class Evaluation(ABC):

    def __init__(self, title, max_score):
        self.title = title
        self.max_score = max_score

    @abstractmethod
    def evaluate(self, score):
        pass


class QuizEvaluation(Evaluation):

    def evaluate(self, score):
        print(f"Evaluando Quiz '{self.title}': {score}/{self.max_score}")
        return score


class ProjectEvaluation(Evaluation):

    def evaluate(self, score):
        print(f"Evaluando Proyecto '{self.title}': {score}/{self.max_score}")
        return score


class ExamEvaluation(Evaluation):

    def evaluate(self, score):
        print(f"Evaluando Examen '{self.title}': {score}/{self.max_score}")
        return score


class EvaluationFactory:

    @staticmethod
    def create_evaluation(eval_type, title, max_score):

        if eval_type == "quiz":
            return QuizEvaluation(title, max_score)

        elif eval_type == "project":
            return ProjectEvaluation(title, max_score)

        elif eval_type == "exam":
            return ExamEvaluation(title, max_score)

        else:
            raise ValueError("Tipo de evaluación no soportado")


# =========================================================
# SISTEMA LMS SIMPLIFICADO
# =========================================================

class LMS:

    def __init__(self):
        self.users = []
        self.courses = []
        self.grades = {}

    def add_user(self, user):
        self.users.append(user)

    def add_course(self, course):
        self.courses.append(course)

    def save_grade(self, student_name, grade):
        self.grades[student_name] = grade

    def get_grades(self):
        return self.grades
