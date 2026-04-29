# SPEC - Cálculo de notas con media, mediana y uso de GitHub MCP

## Problema
Se necesita una aplicación sencilla para calcular la nota final de un alumno a partir de tres notas. El usuario podrá elegir si quiere calcular la media o la mediana. Además, el proyecto debe quedar publicado en GitHub y acompañado por una prueba real del uso de GitHub MCP sobre el repositorio.

## Solución esperada
El programa solicitará:
- nombre del alumno
- nota 1
- nota 2
- nota 3
- tipo de cálculo: `media` o `mediana`

Después:
- usará `tools_notas.py` para calcular el resultado numérico
- mostrará el nombre del alumno
- mostrará el tipo de cálculo elegido
- mostrará el resultado numérico
- mostrará `Aprobado` o `Suspenso`

## Archivos principales esperados
- `main.py`
- `tools_notas.py`
- `test_main.py`
- `PRD.md`
- `SPEC.md`
- `AGENTS.md`
- `README.md`

## Criterios de aceptación
- `calcular_media(notas)` devuelve la media correcta
- `calcular_mediana(notas)` devuelve la nota central tras ordenar tres notas
- `main.py` importa y usa `calcular_media` y `calcular_mediana`
- El programa permite elegir entre media o mediana
- Si el resultado numérico es mayor o igual que 5, muestra `Aprobado`
- Si el resultado numérico es menor que 5, muestra `Suspenso`
- El proyecto queda documentado y preparado para GitHub
- La entrega incluye evidencia real del uso de GitHub MCP
