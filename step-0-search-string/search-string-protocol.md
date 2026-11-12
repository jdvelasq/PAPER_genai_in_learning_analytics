# Diseño iterativo de la cadena de búsqueda

## Propósito

Diseña una cadena de búsqueda para Scopus que recupere de forma **exhaustiva** los documentos potencialmente relevantes para el tema de revisión proporcionado. La meta de esta etapa es maximizar la sensibilidad de la recuperación; **no** es seleccionar, evaluar la calidad ni decidir los estudios definitivos. La selección de estudios será una etapa posterior e independiente.

## Parámetro obligatorio

Recibe el parámetro `executor`, con uno de estos valores exactos: `codex`, `claude` o `gemini`. El valor `codex` corresponde al proceso realizado por ChatGPT/Codex.

Si `executor` no fue suministrado, detente y pregunta: **«¿Qué executor debo usar: `codex`, `claude` o `gemini`?»** No propongas ni modifiques una cadena hasta recibir la respuesta.

Cada executor diseña y mantiene su propia cadena, sin reutilizar ni sobrescribir la de los demás. Usa exclusivamente el directorio que corresponda:

| `executor` | Directorio |
| --- | --- |
| `codex` | `step-0-search-string/codex/` |
| `claude` | `step-0-search-string/claude/` |
| `gemini` | `step-0-search-string/gemini/` |

## Proceso

1. Identifica los conceptos centrales del tema de revisión y construye una cadena inicial para Scopus. Emplea sinónimos, variantes ortográficas, acrónimos y términos técnicos pertinentes; combina equivalentes con `OR` y conceptos distintos con `AND`. Prioriza los campos y la sintaxis de Scopus, por ejemplo `TITLE-ABS-KEY(...)`.
2. En la primera iteración, registra únicamente la cadena inicial en `step-0-search-string/<executor>/log.md`.
3. El usuario ejecutará la búsqueda en Scopus y reportará los resultados de cada iteración. Conserva los archivos o información de resultados que el usuario aporte en `step-0-search-string/<executor>/`.
4. Con cada nuevo resultado de Scopus, revisa la recuperación de forma iterativa. Busca mejorar la exhaustividad: incorpora términos relevantes ausentes, sinónimos, denominaciones históricas o variantes detectadas. No uses restricciones que puedan excluir documentos pertinentes solo para reducir el volumen de resultados.
5. Tras revisar cada resultado, decide si la cadena converge. Hay convergencia cuando la revisión no identifica cambios razonables que aumenten materialmente la recuperación exhaustiva de documentos relevantes. La cantidad de resultados por sí sola no determina la convergencia.
6. Repite el ciclo hasta que converja. La decisión final sobre qué documentos se incluirán no pertenece a este proceso.

## Formato obligatorio de `log.md`

Mantén un único archivo cronológico: `step-0-search-string/<executor>/log.md`. No borres ni reescribas registros anteriores.

### Iteración 1

Registra solamente:

````markdown
## Iteración 1

### Cadena inicial
```text
<cadena de búsqueda para Scopus>
```
````

### Iteración 2 y posteriores

Cada registro debe contener:

````markdown
## Iteración <n>

- Artículos recuperados: <cantidad total reportada por Scopus>
- Estado: <Converge | No converge>
- Explicación: <solo si es necesaria; máximo 100 palabras>

### <Nueva cadena sugerida | Cadena final seleccionada>
```text
<cadena de búsqueda para Scopus>
```
````

- Si el estado es **No converge**, escribe **Nueva cadena sugerida**.
- Si el estado es **Converge**, escribe **Cadena final seleccionada**.
- Si no se requiere explicación, omite el campo `Explicación`.
- La explicación nunca debe superar 100 palabras.

## Reglas de colaboración

- ChatGPT, Claude y Gemini realizarán este proceso de manera independiente; no intentes armonizar sus cadenas durante esta fase.
- Declara con claridad la cadena completa sugerida en cada iteración para que el usuario pueda copiarla y ejecutarla en Scopus.
- No inventes cantidades de artículos ni resultados. Espera siempre el reporte del usuario para registrar una iteración posterior a la primera.
- Antes de declarar convergencia, comprueba que la cadena todavía cubra los conceptos, sinónimos y variantes relevantes identificados durante las iteraciones.
