# Diseño iterativo de la cadena de búsqueda

## Propósito

Diseña una cadena de búsqueda para Scopus que recupere de forma **exhaustiva** los documentos potencialmente relevantes para el tema de revisión proporcionado. La meta de esta etapa es maximizar la sensibilidad de la recuperación; **no** es seleccionar, evaluar la calidad ni decidir los estudios definitivos. La selección de estudios será una etapa posterior e independiente.

## Parámetros obligatorios

Recibe estos dos parámetros:

- `executor`: uno de estos valores exactos: `codex`, `claude` o `gemini`. El valor `codex` corresponde al proceso realizado por ChatGPT/Codex.
- `folder`: ruta del directorio de ejecución donde deben leerse y escribirse el `log.md` y los resultados de Scopus.

Si falta cualquiera de los dos parámetros, detente y pregunta por el parámetro faltante. Para `executor`, pregunta: **«¿Qué executor debo usar: `codex`, `claude` o `gemini`?»** Para `folder`, pregunta: **«¿Qué folder de ejecución debo usar?»** No propongas ni modifiques una cadena hasta recibir ambos.

El `folder` debe corresponder al `executor`, salvo que el usuario indique explícitamente otra ruta:

| `executor` | Directorio |
| --- | --- |
| `codex` | `step-0-search-string/codex/` |
| `claude` | `step-0-search-string/claude/` |
| `gemini` | `step-0-search-string/gemini/` |

Usa el valor recibido en `folder` como ruta efectiva en todas las operaciones. No sustituyas silenciosamente el `folder` por otra ruta.

## Proceso

1. Lee obligatoriamente [`research-questions.md`](../research-questions.md) para identificar el objetivo general y las preguntas de investigación.
2. Lee obligatoriamente [`aims-and-scope.md`](../aims-and-scope.md) para alinear la búsqueda con el alcance de IEEE-RITA.
3. A partir de esas dos fuentes, identifica los conceptos centrales y construye una cadena inicial para Scopus. Emplea sinónimos, variantes ortográficas, acrónimos y términos técnicos pertinentes; combina equivalentes con `OR` y conceptos distintos con `AND`. Prioriza los campos y la sintaxis de Scopus, por ejemplo `TITLE-ABS-KEY(...)`.
4. En la primera iteración, registra únicamente la cadena inicial en `<folder>/log.md`.
5. Detente y solicita al usuario que ejecute la cadena inicial en Scopus. Indica explícitamente que el resultado exportado debe almacenarse como `<folder>/01.csv` y que el usuario debe reportar la cantidad total de artículos recuperados. No avances a la siguiente iteración sin ese archivo y ese reporte.
6. Con cada nuevo resultado de Scopus, revisa la recuperación de forma iterativa. Busca mejorar la exhaustividad: incorpora términos relevantes ausentes, sinónimos, denominaciones históricas o variantes detectadas. No uses restricciones que puedan excluir documentos pertinentes solo para reducir el volumen de resultados.
7. Tras revisar cada resultado, registra la iteración y decide si la cadena converge. Hay convergencia cuando la revisión no identifica cambios razonables que aumenten materialmente la recuperación exhaustiva de documentos relevantes. La cantidad de resultados por sí sola no determina la convergencia.
   La evaluación de convergencia debe basarse en la revisión del título, el abstract, las author keywords y las index keywords de los registros exportados desde Scopus. No declares convergencia usando únicamente el número de resultados o los títulos. Si la exportación no contiene abstract y keywords, detente y solicita una nueva exportación antes de evaluar la convergencia.
8. Si no converge, presenta la nueva cadena, detente y vuelve a solicitar al usuario la ejecución en Scopus y el reporte de resultados. Si converge, registra la cadena final y termina el proceso. La decisión final sobre qué documentos se incluirán no pertenece a este proceso.

9. En cada iteración, muestra siempre en la respuesta la cadena completa de búsqueda correspondiente a esa iteración, incluso cuando también se haya registrado en `log.md`. La cadena debe aparecer en un bloque de código `text`, sin abreviarla ni sustituir partes por puntos suspensivos, para que el usuario pueda copiarla directamente en Scopus.
10. Formatea siempre las cadenas de Scopus en varias líneas legibles: usa una línea para `TITLE-ABS-KEY(`, separa los bloques conceptuales mediante `AND`, coloca cada término o grupo de sinónimos en líneas sucesivas con indentación y conserva los operadores `OR` al final o al inicio de forma consistente. Nunca presentes una cadena completa en una sola línea.
11. Debido a que Scopus no distingue entre mayúsculas y minúsculas, escribe todos los términos de búsqueda en minúsculas. No repitas términos equivalentes o idénticos dentro de un mismo bloque. Mantén en mayúsculas todos los operadores booleanos (`AND`, `OR`, `NOT`) y los identificadores sintácticos de Scopus, como `TITLE-ABS-KEY`.
12. Cuando incluyas un modelo, sistema o producto específico de IA generativa —por ejemplo, `chatgpt`—, revisa e incluye también sus equivalentes y competidores relevantes. No privilegies un proveedor de forma aislada. Considera, según su pertinencia y el periodo de la revisión, variantes como `claude`/`anthropic`, `grok`/`xai`, `gemini`/`bard`, `copilot`/`microsoft copilot`, `llama`, `mistral`, `deepseek`, `qwen` y otros modelos equivalentes. No uses nombres de empresas genéricos como `microsoft`, `meta` o `google` sin asociarlos a un modelo o producto específico. Mantén además los términos generales como `large language model*`, `llm*`, `foundation model*`, `generative ai` y `genai`, porque muchos estudios no mencionan una marca.

## Formato obligatorio de `log.md`

Mantén un único archivo cronológico: `<folder>/log.md`. No borres ni reescribas registros anteriores.

Cada nueva iteración debe agregarse exclusivamente al final de `<folder>/log.md`, después de todo el contenido existente. La modificación debe realizarse mediante una operación de append al final del archivo: conserva literalmente todo el contenido previo y escribe el nuevo bloque después del último carácter existente. Nunca insertes una iteración entre registros anteriores ni reordenes, reemplaces o reconstruyas el archivo completo.

Antes de finalizar una actualización, verifica que los encabezados de iteración aparezcan en orden estrictamente cronológico (`Iteración 1`, `Iteración 2`, `Iteración 3`, etc.) y que la nueva iteración sea el último encabezado del archivo.

Procedimiento obligatorio para cada iteración, incluida la primera:

1. Si `log.md` ya existe, lee el archivo completo y localiza el último encabezado `## Iteración <n>`; si no existe, establece la nueva iteración como `Iteración 1`.
2. Lee también las últimas líneas del archivo para confirmar cuál es su contenido final.
3. Genera primero un archivo individual `<folder>/iteration-<n+1>.md` que contenga exclusivamente el bloque completo de la nueva iteración, incluyendo su encabezado, resultado, estado, explicación y cadena.
4. Verifica el archivo individual: comprueba que contiene una sola iteración, la cadena completa y el formato multilínea correcto.
5. Agrega el contenido del archivo individual únicamente al final de `log.md` mediante una operación de append. No reconstruyas, reordenes ni modifiques el contenido anterior de `log.md`.
6. Verifica nuevamente que `## Iteración <n+1>` sea el último encabezado de `log.md` y que no existan encabezados posteriores.
7. Solo después de verificar correctamente el append y el orden cronológico, elimina el archivo individual temporal `<folder>/iteration-<n+1>.md`.

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
- Muestra la cadena completa en pantalla en cada iteración, además de registrarla en el `log.md` correspondiente.
- Presenta y registra las cadenas en formato multilínea legible; no uses una sola línea para la cadena completa.
- Escribe todos los términos en minúsculas, elimina términos repetidos y conserva en mayúsculas los operadores (`AND`, `OR`, `NOT`) y los identificadores sintácticos de Scopus, como `TITLE-ABS-KEY`.
- Si la cadena contiene un modelo o producto específico, comprueba la cobertura simétrica de otros modelos y proveedores relevantes antes de declararla completa o convergente.
- Agrega cada nueva iteración al final del `log.md`; no la insertes en otra posición del archivo.
- Verifica el orden cronológico de todos los encabezados antes de terminar la actualización.
- No inventes cantidades de artículos ni resultados. Espera siempre el reporte del usuario para registrar una iteración posterior a la primera.
- Después de la cadena inicial, recuerda explícitamente que el resultado de Scopus debe guardarse como `01.csv` dentro del `folder` correspondiente. Para las iteraciones posteriores, utiliza la numeración secuencial `02.csv`, `03.csv`, etc.
- Para cada iteración posterior a la primera, requiere una exportación de Scopus que incluya, como mínimo, título, abstract, author keywords e index keywords. Usa esos campos para identificar términos ausentes, variantes y posibles mejoras de exhaustividad.
- Antes de declarar convergencia, comprueba que la cadena todavía cubra los conceptos, sinónimos y variantes relevantes identificados durante las iteraciones.
