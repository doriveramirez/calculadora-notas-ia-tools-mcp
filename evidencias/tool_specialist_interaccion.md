# Interacción con el agente Tool Specialist

## Prompt
Actúa como Tool Specialist.

Basándote en `PRD.md` y `SPEC.md`, crea un archivo `tools_notas.py` con dos funciones:
1. `calcular_media(notas)`
2. `calcular_mediana(notas)`

Requisitos:
- `notas` será una lista de tres números
- `calcular_media` devolverá la media aritmética
- `calcular_mediana` devolverá la nota central después de ordenar
- código sencillo
- sin funcionalidades extra

## Respuesta
Se creó `tools_notas.py` con:
- una función `validar_notas(notas)` para comprobar que llega una lista de tres valores numéricos
- `calcular_media(notas)` para devolver la media
- `calcular_mediana(notas)` para devolver la nota central

## Resultado
La lógica de cálculo quedó separada del programa principal, tal como pedía el enunciado.
