# Ejecución del proceso de búsqueda

## Archivos

- [`search-string-protocol.md`](search-string-protocol.md): instrucciones que debe seguir el modelo.
- `codex/`, `claude/` y `gemini/`: carpetas independientes de ejecución.
- `<folder>/log.md`: registro cronológico de las iteraciones.
- `<folder>/scopus-<n>.csv`: resultados exportados desde Scopus para cada iteración.

## Parámetros de ejecución

Cada ejecución debe recibir ambos parámetros:

```text
executor=<codex|claude|gemini>
folder=step-0-search-string/<executor>
```

Ejemplos:

```text
executor=codex
folder=step-0-search-string/codex
```

```text
executor=claude
folder=step-0-search-string/claude
```

```text
executor=gemini
folder=step-0-search-string/gemini
```

El valor `codex` corresponde a ChatGPT/Codex. Cada modelo debe ejecutarse de forma independiente y trabajar únicamente en su propio `folder`.

## Inicio

1. Abre el archivo `search-string-protocol.md` y proporciona al modelo el objetivo y las preguntas de investigación de [`../research-questions.md`](../research-questions.md).
2. Proporciona los parámetros `executor` y `folder`.
3. El modelo genera la cadena inicial y la registra en `<folder>/log.md` como Iteración 1.
4. El modelo se detiene y te solicita ejecutar esa cadena en Scopus.
5. Ejecuta la cadena, guarda el resultado exportado como `<folder>/scopus-1.csv` y reporta al modelo la cantidad total de artículos recuperados.
6. En cada iteración posterior, proporciona el nuevo archivo o sus resultados. El modelo actualizará `log.md`, propondrá una nueva cadena si no converge y volverá a detenerse para solicitarte otra búsqueda.
7. Repite el intercambio hasta que el modelo declare convergencia y registre la cadena final.

## Reglas

- No mezcles resultados entre `codex`, `claude` y `gemini`.
- No borres entradas anteriores de `log.md`.
- No inventes cantidades de resultados; deben proceder de Scopus.
- La selección definitiva de estudios ocurre después de finalizar este proceso de búsqueda exhaustiva.
