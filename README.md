# Calculadora de notas con Tools y GitHub MCP

## Descripción
Aplicación de consola en Python que solicita el nombre de un alumno y tres notas, permite elegir entre calcular la media o la mediana y muestra si el resultado final es aprobado o suspenso. El proyecto incluye también la publicación del repositorio y una evidencia real del uso de GitHub MCP sobre ese repositorio.

## Archivos principales
- `PRD.md`: objetivo y funcionalidades del proyecto.
- `SPEC.md`: comportamiento esperado y criterios de aceptación.
- `AGENTS.md`: definición de los roles usados en la práctica.
- `main.py`: programa principal.
- `tools_notas.py`: funciones externas para calcular media y mediana.
- `test_main.py`: pruebas unitarias.
- `EVIDENCIAS.md`: índice de evidencias.
- `REFLEXION.md`: reflexión final.
- `evidencias/github_mcp_uso.md`: resumen del uso real de GitHub MCP.
- `evidencias/github_mcp_issue_comment.json`: registro de la llamada MCP que añade y verifica un comentario.

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
- Publisher: revisó el proyecto, verificó la publicación en GitHub y dejó una prueba real de GitHub MCP sobre el issue `#1`.

## Evidencias
Las capturas, registros y pruebas del uso de GitHub MCP están dentro de la carpeta `evidencias/`.
