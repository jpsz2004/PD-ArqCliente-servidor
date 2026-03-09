# =========================================================
# PROXY PATTERN
# Control de acceso por rol
# =========================================================

class GradeService:

    def assign_grade(self, student_name, grade):
        print(f"Nota {grade} asignada a {student_name}")


class GradeServiceProxy:

    def __init__(self, user):
        self.user = user
        self.service = GradeService()

    def assign_grade(self, student_name, grade):

        if self.user.role != "professor":
            print("Acceso denegado: solo los profesores pueden asignar notas")
            return

        self.service.assign_grade(student_name, grade)
