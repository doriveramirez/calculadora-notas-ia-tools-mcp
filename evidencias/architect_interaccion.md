# Interacción con el agente Architect

## Prompt
Actúa como Architect. Lee `PRD.md`, `SPEC.md` y `AGENTS.md`.

Tu tarea es proponer la estructura mínima del proyecto en Python e indicar cómo separar la lógica principal de la lógica de cálculo.

## Respuesta
- `main.py` debe encargarse de la entrada por consola y de mostrar el resultado final.
- `tools_notas.py` debe contener `calcular_media(notas)` y `calcular_mediana(notas)`.
- `test_main.py` debe comprobar tanto las funciones externas como la clasificación final.
- `README.md` y el resto de documentos deben recoger la parte de GitHub y Publisher.

## Conclusión
La propuesta del Architect deja claro que la lógica de cálculo debe salir del programa principal y pasar a una tool externa.
