# Calculadora de notas con Tools y preparación para GitHub

## Descripción
Aplicación de consola en Python que solicita el nombre de un alumno y tres notas, permite elegir entre calcular la media o la mediana y muestra si el resultado final es aprobado o suspenso.

## Archivos principales
- `PRD.md`: objetivo y funcionalidades del proyecto.
- `SPEC.md`: comportamiento esperado y criterios de aceptación.
- `AGENTS.md`: definición de los roles usados en la práctica.
- `main.py`: programa principal.
- `tools_notas.py`: funciones externas para calcular media y mediana.
- `test_main.py`: pruebas unitarias.
- `EVIDENCIAS.md`: índice de evidencias.
- `REFLEXION.md`: reflexión final.

## Requisitos
- Python 3 instalado

## Ejecución
```bash
python main.py
```

## Ejemplo de uso
- Nombre: Marta
- Notas: 10, 8, 9
- Tipo de cálculo: media
- Resultado numérico: 9.0
- Resultado: Aprobado

## Trabajo por agentes
- Architect: propuso la estructura del proyecto y la separación de responsabilidades.
- Builder: adaptó `main.py` para usar tools externas.
- Tester: comprobó media, mediana y clasificación final.
- Documenter: organizó la documentación y las evidencias.
- Tool Specialist: creó `tools_notas.py`.
- Publisher: revisó el proyecto, verificó la publicación en GitHub y creó el issue de mejoras futuras.

## Evidencias
Las capturas y registros del proceso están dentro de la carpeta `evidencias/`.
