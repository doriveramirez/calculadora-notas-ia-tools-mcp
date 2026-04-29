# Interacción con el agente Tester

## Prompt
Actúa como Tester.

Revisa `main.py` y `tools_notas.py`.

Comprueba:
1. que `calcular_media` funciona correctamente
2. que `calcular_mediana` funciona correctamente
3. que el programa muestra aprobado si el resultado es >= 5
4. que el programa muestra suspenso si el resultado es < 5

Propón al menos 4 casos de prueba manuales.

## Respuesta
### Criterios comprobados
- `calcular_media` devuelve el valor esperado.
- `calcular_mediana` devuelve la nota central tras ordenar.
- La clasificación final muestra `Aprobado` o `Suspenso` correctamente.

### Casos de prueba manuales
- Ana: `5, 5, 5` -> media `5` -> `Aprobado`
- Luis: `4, 4, 4` -> media `4` -> `Suspenso`
- Marta: `10, 8, 9` -> media `9` -> `Aprobado`
- Pedro: `2, 10, 4` -> mediana `4` -> `Suspenso`

## Resultado
El programa cumple los criterios principales y queda respaldado por pruebas automáticas y manuales.
