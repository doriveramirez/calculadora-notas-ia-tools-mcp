# Reflexión final

## Qué se aprende con esta segunda parte
Esta práctica permite ver que un agente no solo redacta texto, sino que puede apoyarse en funciones externas para delegar una parte concreta del trabajo. En este caso, la media y la mediana se sacan fuera del programa principal para que la lógica quede mejor organizada.

## Papel de las tools
Separar `calcular_media` y `calcular_mediana` en `tools_notas.py` hace más fácil comprobar el funcionamiento, reutilizar el cálculo y mantener `main.py` más claro.

## Papel de la parte de GitHub y MCP
La parte de Publisher sirve para entender que un agente también puede preparar el proyecto para una herramienta externa. Aunque no siempre esté disponible GitHub MCP, el flujo de revisión y preparación sigue teniendo sentido como parte de la entrega.

## Qué mejoraría
Como mejora futura, añadiría una forma de guardar resultados, más validaciones y más pruebas automáticas, pero manteniendo el proyecto sencillo.
