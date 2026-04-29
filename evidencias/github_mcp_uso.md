# Uso real de GitHub MCP

## Servidor utilizado
- Repositorio de referencia: `https://github.com/github/github-mcp-server`
- Endpoint utilizado: `https://api.githubcopilot.com/mcp/`
- Protocolo MCP: `2025-06-18`

## Secuencia ejecutada
- `initialize`
- `notifications/initialized`
- `tools/list`
- `get_me`
- `add_issue_comment`
- `issue_read` con `get_comments`

## Resultado visible
- Repositorio: `https://github.com/doriveramirez/calculadora-notas-ia-tools-mcp`
- Issue usado: `https://github.com/doriveramirez/calculadora-notas-ia-tools-mcp/issues/1`
- Comentario creado por MCP: `https://github.com/doriveramirez/calculadora-notas-ia-tools-mcp/issues/1#issuecomment-4346856335`

## Archivos de prueba
- `evidencias/github_mcp_initialize_and_tools.json`
- `evidencias/github_mcp_issue_comment.json`
- `evidencias/github_mcp_issue_comment.txt`
