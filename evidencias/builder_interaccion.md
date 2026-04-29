# Interacción con el agente Builder

## Prompt
Actúa como Builder.

Modifica `main.py` para usar las funciones del archivo `tools_notas.py`.

Requisitos:
- importar `calcular_media` y `calcular_mediana`
- pedir nombre del alumno
- pedir tres notas
- preguntar si se quiere calcular media o mediana
- mostrar el resultado numérico
- indicar aprobado si el resultado es mayor o igual que 5
- indicar suspenso si es menor que 5
- mantener el código sencillo

## Respuesta
Se adaptó `main.py` para:
- importar las funciones externas
- pedir tres notas por consola
- preguntar el tipo de cálculo
- delegar el cálculo en `tools_notas.py`
- mostrar el resultado final

## Resultado
`main.py` quedó conectado con `tools_notas.py` y cumple la SPEC.
