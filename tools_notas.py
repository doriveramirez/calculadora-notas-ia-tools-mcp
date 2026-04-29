"""Funciones externas para calcular la media o la mediana de tres notas."""


def validar_notas(notas: list[float]) -> None:
    """Comprueba que las notas llegan en una lista de tres valores numéricos."""
    if not isinstance(notas, list):
        raise ValueError("Las notas deben recibirse en una lista.")

    if len(notas) != 3:
        raise ValueError("Se requieren exactamente tres notas.")

    for nota in notas:
        if not isinstance(nota, (int, float)):
            raise ValueError("Cada nota debe ser numérica.")


def calcular_media(notas: list[float]) -> float:
    """Devuelve la media aritmética de tres notas."""
    validar_notas(notas)
    return sum(notas) / len(notas)


def calcular_mediana(notas: list[float]) -> float:
    """Devuelve la nota central tras ordenar tres notas."""
    validar_notas(notas)
    notas_ordenadas = sorted(notas)
    return notas_ordenadas[1]
