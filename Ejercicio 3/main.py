from models import LMS, Professor, Student, EvaluationFactory
from observer import Course, StudentObserver
from strategy import ReportGenerator, PDFReportStrategy, CSVReportStrategy, JSONReportStrategy
from proxy import GradeServiceProxy

# =========================================================
# DEMO DEL SISTEMA
# =========================================================

def main():

    print("\n=== INICIANDO LMS ===")

    lms = LMS()

    # Crear usuarios
    professor = Professor("Dr. López")
    student1 = Student("Ana")
    student2 = Student("Carlos")

    lms.add_user(professor)
    lms.add_user(student1)
    lms.add_user(student2)

    # Crear curso
    course = Course("Patrones de Diseño")
    lms.add_course(course)

    # Suscribir estudiantes a notificaciones
    course.subscribe(StudentObserver(student1))
    course.subscribe(StudentObserver(student2))

    # Crear evaluación usando Factory
    evaluation = EvaluationFactory.create_evaluation(
        "quiz",
        "Parcial 1",
        100
    )

    # Profesor califica
    score = evaluation.evaluate(95)

    # Control de acceso usando Proxy
    proxy = GradeServiceProxy(professor)
    proxy.assign_grade(student1.name, score)

    # Guardar nota
    lms.save_grade(student1.name, score)

    # Notificar estudiantes
    course.notify("Nueva calificación publicada")

    # Generar reporte usando Strategy
    data = lms.get_grades()

    report = ReportGenerator(PDFReportStrategy())
    report.generate_report(data)

    report = ReportGenerator(CSVReportStrategy())
    report.generate_report(data)

    report = ReportGenerator(JSONReportStrategy())
    report.generate_report(data)


if __name__ == "__main__":
    main()
