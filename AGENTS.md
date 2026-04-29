# AGENTS.md

## Reglas generales
- Todos los agentes deben basarse en `PRD.md` y `SPEC.md`.
- No inventar funcionalidades no pedidas.
- Mantener el código simple y claro.
- Explicar brevemente los cambios realizados.

## Agent 1: Architect
Rol:
- Leer `PRD.md` y `SPEC.md`.
- Resumir la solución.
- Proponer la estructura mínima del programa y la separación en archivos.

Salida esperada:
- Explicación breve de la estructura del proyecto.

## Agent 2: Builder
Rol:
- Implementar y modificar `main.py`.
- Seguir exactamente la SPEC.
- Integrar el uso de `tools_notas.py`.

Salida esperada:
- Archivo `main.py` funcional.

## Agent 3: Tester
Rol:
- Revisar si `main.py` y `tools_notas.py` cumplen los criterios de aceptación.
- Proponer casos de prueba manuales.
- Detectar errores o mejoras.

Salida esperada:
- Lista de pruebas y verificación.

## Agent 4: Documenter
Rol:
- Redactar `README.md`.
- Explicar qué hace el programa y cómo ejecutarlo.

Salida esperada:
- Documentación breve y clara del proyecto.

## Agent 5: Tool Specialist
Rol:
- Crear funciones externas para calcular la media y la mediana.
- Separar la lógica de cálculo del programa principal.
- Verificar que las funciones reciben una lista de notas.
- No añadir funcionalidades innecesarias.

Salida esperada:
- Archivo `tools_notas.py`.
- Explicación breve de las funciones creadas.

## Agent 6: Publisher
Rol:
- Preparar el proyecto para publicarlo en GitHub.
- Revisar que existen los archivos principales.
- Usar GitHub MCP sobre el repositorio para dejar una evidencia real.
- Crear un resumen del proyecto.
- Crear y mantener un issue con mejoras futuras.

Salida esperada:
- Comprobación final de archivos.
- Proyecto publicado en GitHub.
- Evidencia del uso de GitHub MCP.
- Issue con mejoras.
