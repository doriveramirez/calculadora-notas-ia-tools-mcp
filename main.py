"""Calculadora de notas con uso de tools externas."""

from tools_notas import calcular_media, calcular_mediana


def parse_grade(value: str) -> float:
    """Convierte una entrada en nota numérica y valida su rango."""
    try:
        grade = float(value)
    except ValueError as exc:
        raise ValueError("La nota debe ser un número.") from exc

    if grade < 0 or grade > 10:
        raise ValueError("La nota debe estar entre 0 y 10.")

    return grade


def determine_result(score: float) -> str:
    """Devuelve Aprobado o Suspenso según el resultado numérico."""
    return "Aprobado" if score >= 5 else "Suspenso"


def request_calculation_option() -> str:
    """Pide si se quiere calcular la media o la mediana."""
    while True:
        option = input("¿Qué quieres calcular? media/mediana: ").strip().lower()
        if option in {"media", "mediana"}:
            return option
        print("Opción no válida. Escribe 'media' o 'mediana'.")


def request_grades() -> list[float]:
    """Solicita tres notas válidas por consola."""
    grades = []
    for index in range(1, 4):
        while True:
            try:
                grade = parse_grade(input(f"Introduce la nota {index}: ").strip())
                grades.append(grade)
                break
            except ValueError as error:
                print(f"Entrada inválida: {error}")
    return grades


def main() -> None:
    """Ejecuta el flujo principal del programa."""
    student_name = input("Introduce el nombre del alumno: ").strip()
    while not student_name:
        student_name = input("El nombre no puede estar vacío. Introduce el nombre del alumno: ").strip()

    grades = request_grades()
    option = request_calculation_option()

    if option == "mediana":
        numeric_result = calcular_mediana(grades)
    else:
        numeric_result = calcular_media(grades)

    result = determine_result(numeric_result)

    print("\nAlumno:", student_name)
    print("Tipo de cálculo:", option)
    print("Resultado numérico:", round(numeric_result, 2))
    print("Resultado:", result)


if __name__ == "__main__":
    main()
