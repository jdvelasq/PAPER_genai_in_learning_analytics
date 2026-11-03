# Search Strategy Refinement Log

## Iteration 0

**Timestamp:** 2026-11-03 08:44 (America/Bogota, UTC-05:00)

**Search String:** cadena 00, **ejecutada** en Scopus; produjo el CSV analizado (`scopus-0.csv`, 885 registros).

```sql
TITLE-ABS-KEY (
  "generative AI" OR
  "generative artificial intelligence" OR
  GenAI OR
  "large language model*" OR
  LLM OR LLMs OR
  "foundation model*" OR
  "agentic AI" OR
  "agentic artificial intelligence" OR
  "AI agent*" OR
  "autonomous agent*" OR
  "multi-agent system*" OR
  "multiagent system*"
)
AND
TITLE-ABS-KEY (
  "learning analytics" OR
  "teaching analytics" OR
  "educational data mining" OR
  "academic analytics"
)
```

**Evaluation:**

- Volumen y calidad de los datos: 885 registros, todos con EID único y sin duplicados. 749 tienen DOI (todos únicos) y 136 no tienen DOI, por lo que el EID será la clave principal de comparación entre iteraciones. 2 registros no tienen resumen.
- Perfil temporal: 832 de 885 registros son de 2024 o posterior; 745 son de 2025 o posterior y 488 de 2026. 31 registros son de 2022 o anterior. Hay 39 registros con año 2027 y 24 en estado "Article in press" (metadatos de Scopus; no se ajustaron).
- Tipo documental: 460 conference paper, 253 article, 67 conference review, 41 review, 41 book chapter, 14 editorial, 5 book, 3 note, 1 data paper.
- Bloque 2 (analítica educativa): está dominado por "learning analytics", que aparece en 775 registros; 742 se recuperan solo por ese término. "educational data mining" aparece en 124 (93 solo por ese término). "teaching analytics" aparece en 8 (7 exclusivos) y "academic analytics" en 4 (3 exclusivos). Ninguno de los términos poco frecuentes es redundante, así que no se justifica retirarlos.
- Bloque 1 (IA generativa y agéntica): 830 registros contienen al menos un término de GenAI, LLM, foundation model o agentic AI. Frecuencias por término: "large language model*" 396, "generative AI" 390, LLM 234, "generative artificial intelligence" 219, LLMs 210, GenAI 164, "multi-agent system*" 56, "AI agent*" 21, "agentic AI" 19, "multiagent system*" 18, "autonomous agent*" 16, "agentic artificial intelligence" 6, "foundation model*" 5.
- Fuerza de la coincidencia: 437 registros coinciden con ambos bloques en título o palabras clave de autor. 153 tienen el bloque 1 en título/keywords de autor y el bloque 2 solo en resumen o keywords indexadas; 149 al revés; y 139 coinciden con ambos bloques solo en resumen o keywords indexadas. Esos 139 son los candidatos con mayor probabilidad de ser coincidencia terminológica sin pertinencia temática plena (no revisados uno a uno).
- Posibles falsos positivos y ruido:
  - 67 registros "Conference review" parecen ser frentes de volúmenes de proceedings (65 por heurística de título; 2 más —"Big Data III: Learning, Analytics, and Applications" y un volumen DELFI 2023— por inspección de títulos). Su resumen enumera múltiples trabajos, por lo que coinciden con ambos bloques sin ser un estudio sobre el tema.
  - 52 registros satisfacen el bloque 1 solo mediante "AI agent*", "autonomous agent*" o "multi-agent system*", sin ningún término de GenAI/LLM/agentic AI. De ellos, 31 son de 2024 o anteriores y 21 de 2025 o posteriores. Según la lectura de sus títulos, la mayoría son sistemas multiagente clásicos en educación (tutores inteligentes, arquitecturas de monitoreo), no IA agéntica basada en modelos de lenguaje; solo 2 contienen vocabulario LLM o agéntico. Son temáticamente cercanos pero de pertinencia discutible para "Generative AI y Agentic AI"; la decisión de mantenerlos o restringirlos queda pendiente.
  - 7 registros no satisfacen literalmente uno de los bloques tras normalizar guiones (p. ej., "Agentic RAG", "Artificial intelligence agent", un artículo sobre criptografía y aprendizaje automático). Scopus los recuperó por un comportamiento de procesamiento de la consulta que no pude reproducir con coincidencia literal (equivalencias o variantes morfológicas); no se confirmó la causa.
- Vocabulario presente en el corpus que no está en la cadena (frecuencia en título/resumen/keywords): ChatGPT 94 (24 como keyword de autor), retrieval-augmented generation 34 (13 como keyword de autor), agentic 27, prompt engineering 27, GPT-4 49, Gemini 20, Llama 22, "AI tutor" 19, chatbot 71. Como el CSV solo contiene documentos ya recuperados por la cadena 00, no permite medir los documentos omitidos; solo indica vocabulario que podría capturar documentos que no usan los términos genéricos.
- En el bloque 2, "educational analytics" (4), "student analytics" (2), "learner analytics" (2) y "teacher analytics" (2) aparecen con frecuencia muy baja; no hay evidencia en este CSV de un vacío de cobertura en ese bloque.

**Changes:** propuesta (**no ejecutada**) para la cadena 01. Se conserva íntegra la cadena 00 y solo se agregan tres términos al bloque 1; el bloque 2 no se modifica; no se elimina ningún término.

```sql
TITLE-ABS-KEY (
  "generative AI" OR
  "generative artificial intelligence" OR
  GenAI OR
  "large language model*" OR
  LLM OR LLMs OR
  "foundation model*" OR
  "agentic AI" OR
  "agentic artificial intelligence" OR
  "AI agent*" OR
  "autonomous agent*" OR
  "multi-agent system*" OR
  "multiagent system*" OR
  ChatGPT OR
  agentic OR
  "retrieval-augmented generation"
)
AND
TITLE-ABS-KEY (
  "learning analytics" OR
  "teaching analytics" OR
  "educational data mining" OR
  "academic analytics"
)
```

**Rationale:**

- La cadena 01 es sintácticamente un superconjunto de la cadena 00, por lo que debería recuperar todos los registros de la iteración 0 y los efectos de la modificación se pueden atribuir a los tres términos nuevos. Si faltara alguno de los 885 EID, se tratará como inconsistencia de la exportación y no como efecto de la cadena.
- ChatGPT: es la herramienta nominada con más frecuencia en el corpus (94 registros) y un registro que nombre ChatGPT sin usar "generative AI", "LLM" o similares no puede recuperarse con la cadena 00.
- agentic: 27 registros contienen la raíz, frente a 19 que contienen "agentic AI"; la raíz sola capturaría variantes como "agentic RAG", "agentic workflow" o "agentic system", y al menos un registro recuperado ("Agentic RAG") no satisface literalmente ningún término del bloque 1.
- retrieval-augmented generation: 34 registros lo contienen (13 como keyword de autor); es una arquitectura de LLM y puede aparecer sin los términos genéricos.
- No se modifican las decisiones sobre sistemas multiagente clásicos ni sobre los frentes de proceedings. Primero se mide el efecto de ampliar el vocabulario; la restricción de precisión se evalúa en la iteración 1 con la comparación por EID, ya que su impacto sobre la recuperación es cuantificable (52 registros solo por términos de agentes; 10 registros recuperados solo por "teaching analytics" o "academic analytics" en el otro bloque) y todavía no hay un criterio de alcance confirmado.
- En la iteración 1 se medirán: registros nuevos, conservados y perdidos (por EID); qué término nuevo recuperó cada registro nuevo; y la pertinencia temática de los registros nuevos revisando título y resumen.

**Validation Results:**

- Registros: 885; EID únicos: 885; duplicados por EID: 0; DOI presentes: 749 (únicos: 749); sin DOI: 136; sin resumen: 2.
- Año 2027: 39 registros; "Article in press": 24; con citas > 0: 360.
- Comparación con iteraciones anteriores: no aplica (esta es la primera iteración); no se calculan registros nuevos, conservados ni perdidos.
- Las cifras anteriores se calcularon con scripts sobre el CSV exportado. Las coincidencias por término se aproximaron con expresiones regulares sobre título, resumen, keywords de autor y keywords indexadas, tratando los guiones como espacios; difieren del procesamiento interno de Scopus en 7 registros (ver Evaluation).
- La clasificación de pertinencia de los 52 registros "solo agentes" se basa en la lectura de sus títulos, no en una revisión de resúmenes ni en una validación con dos revisores.

**Convergence Status:** `continue`

## Iteration 1

**Timestamp:** 2026-11-03 ~08:48 (America/Bogota, UTC-05:00; hora aproximada, corregida en la Iteration 2: el valor original, 09:05, se escribió sin consultar el reloj y era posterior a la hora real)

**Search String:** cadena 01, **ejecutada** en Scopus; produjo el CSV analizado (`scopus-1.csv`, 933 registros). Es la cadena 00 más tres términos en el bloque 1.

```sql
TITLE-ABS-KEY (
  "generative AI" OR
  "generative artificial intelligence" OR
  GenAI OR
  "large language model*" OR
  LLM OR LLMs OR
  "foundation model*" OR
  "agentic AI" OR
  "agentic artificial intelligence" OR
  "AI agent*" OR
  "autonomous agent*" OR
  "multi-agent system*" OR
  "multiagent system*" OR
  ChatGPT OR
  agentic OR
  "retrieval-augmented generation"
)
AND
TITLE-ABS-KEY (
  "learning analytics" OR
  "teaching analytics" OR
  "educational data mining" OR
  "academic analytics"
)
```

**Evaluation:**

- Comparación por EID con la iteración 0: 48 registros nuevos, 885 conservados y 0 perdidos. Los 885 EID de la cadena 00 están en la cadena 01, como se esperaba de un superconjunto. El aumento es de 5,4 %.
- Atribución de los nuevos por término (cada uno se recupera por un solo término, sin solapes; ninguno contiene términos de la cadena 00): ChatGPT 31, agentic 11, retrieval-augmented generation 6.
- **ChatGPT (31):** el término aporta documentos que la cadena 00 no podía ver. De los 125 registros de la cadena 01 que mencionan ChatGPT, 31 (24,8 %) no estaban en la iteración 0. En 12 de los 31 aparece en el título o en las palabras clave de autor, y en 19 solo en el resumen o las palabras clave indexadas. Entre los claramente pertinentes por título están "Class integration of ChatGPT and learning analytics for higher education", "The Feasibility of Utilizing ChatGPT in Learning Analytics for the Identification of At-Risk Students" y "ChatGPT-Assisted Codebook Design for Learning Analytics Datasets in Multiple Languages". Una parte de los 19 restantes menciona ChatGPT solo como ejemplo dentro de una lista de herramientas, o forma parte de volúmenes de proceedings.
- **agentic (11):** es un fallo de precisión confirmado. Los 11 registros nuevos lo contienen únicamente en el resumen y en 10 se usa en el sentido de agencia humana ("agentic engagement", "agentic learning", "agentic students", "less agentic teachers", dispositivos "inherently agentic"), no de IA agéntica. Solo uno, "AI-Guided Reflection to Bridge Formal Learning and Work" (2027), lo usa en sentido de IA ("agentic companions"). La justificación de la iteración 0 (capturar "agentic RAG", "agentic workflow") no se confirmó con estos datos. Siete de los 11 son de 2022 o anteriores.
- **retrieval-augmented generation (6):** cinco describen o usan sistemas o estudios basados en RAG en educación (p. ej., "EduFlex", "Rise: A Retrieval-Augmented Generation Enhanced Immersive System for Education") y el sexto es el volumen de proceedings SDS 2026; cuatro de los seis lo tienen en título o palabras clave de autor. Es el término de mayor pertinencia por documento, pero de poco volumen.
- **Ruido por proceedings:** de los 48 nuevos, 7 son "Conference review" que parecen volúmenes completos (6 por ChatGPT y 1 por RAG). En total, la cadena 01 tiene 74 registros de ese tipo (67 de la iteración 0 más 7). Por sus títulos, todos parecen frentes de volumen y no estudios; no se revisaron individualmente.
- Perfil temporal de los nuevos: 2017: 1; 2021: 4; 2022: 2; 2023: 7; 2024: 7; 2025: 9; 2026: 17; 2027: 1. 26 de los 48 tienen términos del bloque 2 en título o palabras clave de autor.
- Candidatos adicionales evaluados con el CSV: en la cadena 01 los registros que mencionan Gemini (20), Llama (19), DeepSeek (10), Claude (13) o Copilot (10) ya estaban todos en la iteración 0 (0 nuevos en cada caso). Para "GPT" (85 registros) solo 3 son nuevos, y para "GPT-4/3.5/4o" (54), 2. Esto no mide los documentos que siguen omitidos, pero no da evidencia de que los nombres de otros modelos aporten recuperación. "chatbot*" (78), "AI tutor*" (21) y "AI-powered" (151) son conceptos más amplios que GenAI, con alto riesgo de coincidencia terminológica sin pertinencia. Revisión (2026-11-03, tras la Iteration 2): la inferencia de que los nombres de otros modelos no aportarían recuperación era incorrecta. Un registro que menciona Gemini o Claude sin ningún término genérico de la cadena no puede aparecer en este CSV, por construcción; "0 nuevos" no es evidencia de ausencia. El mismo mecanismo que aportó 31 registros con ChatGPT y 14 con "GPT*" se aplica a esos nombres.
- Sin cambios respecto a la iteración 0: los 52 registros recuperados solo por términos de agentes clásicos siguen en el corpus (no se tocaron).

**Changes:** propuesta (**no ejecutada**) para la cadena 02. Respecto a la cadena 01: (1) se elimina "agentic"; (2) se agrega "GPT*". Se conservan ChatGPT y "retrieval-augmented generation". No se aplica ningún filtro por tipo de documento. Revisión: la propuesta original de esta iteración incluía `AND NOT DOCTYPE ( cr )`; se retiró antes de ejecutarla por indicación del usuario, que señaló que el procedimiento no permite restringir por tipo de documento. Los volúmenes de proceedings se tratarán en el cribado posterior, por EID.

```sql
TITLE-ABS-KEY (
  "generative AI" OR
  "generative artificial intelligence" OR
  GenAI OR
  "large language model*" OR
  LLM OR LLMs OR
  "foundation model*" OR
  "agentic AI" OR
  "agentic artificial intelligence" OR
  "AI agent*" OR
  "autonomous agent*" OR
  "multi-agent system*" OR
  "multiagent system*" OR
  ChatGPT OR
  "GPT*" OR
  "retrieval-augmented generation"
)
AND
TITLE-ABS-KEY (
  "learning analytics" OR
  "teaching analytics" OR
  "educational data mining" OR
  "academic analytics"
)
```

**Rationale:**

- Eliminar "agentic" tiene una pérdida acotada y conocida: 11 registros, 10 de ellos de uso no relacionado con IA; el 11.º ("agentic companions") se pierde, pero la cadena conserva "agentic AI" y "agentic artificial intelligence". Se evaluó el impacto antes de retirar el término.
- No se filtra por tipo de documento. Los 74 registros "Conference review" (aparentemente volúmenes de proceedings, no revisados individualmente) permanecen en la cadena y se marcarán por EID en el cribado. La pérdida esperada por la eliminación de "agentic" es de 11 registros, de modo que la base esperada antes de las adiciones es de 922.
- Agregar "GPT*": ChatGPT recuperó 31 registros que la cadena 00 no veía; la variante de modelo es la extensión más directa del mismo mecanismo. Es una prueba acotada: el CSV de la cadena 01 no da evidencia de que aporte muchos (solo 3 de 85 registros con "GPT" son nuevos), así que se espera un rendimiento bajo. No se verificó cómo Scopus procesa el comodín con "GPT-4"; el CSV lo mostrará.
- No se agregan Gemini, Llama, DeepSeek, Claude ni Copilot: ya estaban todos en la iteración 0, sin evidencia de omisiones, y varios son homónimos de palabras comunes.
- No se modifica el bloque 2: no hay evidencia en los CSV de un vacío de cobertura en él.
- Criterio para la iteración 2: se declarará convergencia si, respecto a la base esperada, los documentos nuevos son pocos (se espera <2 %), poco pertinentes y la pérdida coincide con la prevista. En ese caso la cadena 02 quedará como cadena final validada.

**Validation Results:**

- Registros: 933; EID únicos: 933; duplicados por EID: 0; DOI presentes: 787 (únicos: 787); sin DOI: 146. Las columnas del CSV son idénticas a las de la iteración 0.
- Comparación con la iteración 0 (por EID): nuevos 48; conservados 885; perdidos 0.
- Nuevos por término: ChatGPT 31, agentic 11, RAG 6 (sin solapes). Nuevos de tipo Conference review: 7. Registros de tipo Conference review en total: 74.
- Predicción verificable para la cadena 02: perdidos 11 (los registros recuperados solo por "agentic"); base esperada 922 antes de las adiciones.
- Las coincidencias por término se aproximaron con expresiones regulares sobre título, resumen, palabras clave de autor y palabras clave indexadas, tratando los guiones como espacios. La evaluación de pertinencia se basa en lectura de títulos y de contextos del resumen, sin revisión de textos completos ni validación con dos revisores.

**Convergence Status:** `continue`

## Iteration 2

**Timestamp:** 2026-11-03 08:54 (America/Bogota, UTC-05:00)

**Search String:** cadena 02, **ejecutada** en Scopus; produjo el CSV analizado (`scopus-2.csv`, 936 registros). Es la cadena 01 sin "agentic" y con "GPT*"; sin filtros por tipo de documento.

```sql
TITLE-ABS-KEY (
  "generative AI" OR
  "generative artificial intelligence" OR
  GenAI OR
  "large language model*" OR
  LLM OR LLMs OR
  "foundation model*" OR
  "agentic AI" OR
  "agentic artificial intelligence" OR
  "AI agent*" OR
  "autonomous agent*" OR
  "multi-agent system*" OR
  "multiagent system*" OR
  ChatGPT OR
  "GPT*" OR
  "retrieval-augmented generation"
)
AND
TITLE-ABS-KEY (
  "learning analytics" OR
  "teaching analytics" OR
  "educational data mining" OR
  "academic analytics"
)
```

**Evaluation:**

- La predicción de la iteración 1 se cumplió exactamente: los 11 registros perdidos respecto a la cadena 01 son los mismos 11 que se habían identificado como recuperados solo por "agentic"; no se perdió ningún otro. Se conservan los 922 registros restantes y los 885 de la iteración 0 siguen todos presentes (0 perdidos respecto a la cadena 00).
- Nuevos respecto a la cadena 01: 14 registros, todos recuperados por "GPT*" (en todos hay un término que empieza por "gpt" en título, resumen o palabras clave). Equivalen a 1,5 % de la base de 922 conservada; el aumento respecto a la iteración anterior fue de 5,4 % (48 registros) y ahora es de 1,5 %.
- Pertinencia de los 14 nuevos (lectura de títulos y del contexto en el resumen; no es una revisión de texto completo):
  - 8 usan un modelo GPT como herramienta en el análisis educativo, p. ej. "Towards Learning Analytics for Interdisciplinary Learning: Leveraging Knowledge-empowered Fine-Tuned GPT Models", "Intelligent Feedback Analytics: Hybrid LSTM-GPT Framework for Educational Improvement", "Enhancing Data Extraction from Student Handwritten Notes Using Multi-Task U-net and GPT-4", y el análisis de escritura con una herramienta basada en GPT.
  - 5 son dudosos o incidentales: GPT mencionado como motivación ("with the rise of chat GPT"), como un modelo comparado (GPT-2 en análisis de sentimiento), como parte de una lista de modelos, o con vínculo débil con analítica educativa (p. ej., "Understanding the Digital Epistemologies of Chat GPT").
  - 1 es un volumen de proceedings ("16th International Conference on Educational Data Mining, EDM 2023").
- Cobertura: se mantienen sin cambios la dependencia de "learning analytics" en el bloque 2 y la de los términos de LLM y GenAI en el bloque 1. No hay evidencia en los tres CSV de términos del bloque 2 omitidos.
- Evidencia para más cambios (corregida el 2026-11-03): la versión original de este punto concluía que no había términos candidatos, apoyándose en que Gemini, Llama, DeepSeek, Claude y Copilot no habían aportado registros nuevos en la iteración 1. Ese argumento era inválido (ver la revisión en la Iteration 1). La evidencia correcta es que ChatGPT (31 nuevos) y "GPT*" (14 nuevos) recuperaron documentos que los términos genéricos no veían, y que en los 936 registros de la cadena 02 los nombres de otros modelos se usan con sentido de modelo de lenguaje: Gemini (20 registros), Llama (19), Claude (13), OpenAI (11), DeepSeek (10), Copilot (10), Qwen (8), Mistral (3) y Anthropic (3). En los contextos del resumen revisados para Claude, Gemini, Llama y Mistral, todos se refieren a modelos de lenguaje. Los conceptos más amplios ("chatbot*", "AI tutor*", "AI-powered") siguen sin incluirse por su alto riesgo de coincidencia terminológica.
- Asuntos que no dependen de la cadena y se resuelven en el cribado, por EID: (a) 75 registros "Conference review" (74 de la iteración 1 más el volumen de EDM 2023), todos aparentemente volúmenes de proceedings, no revisados individualmente; (b) 51 registros recuperados solo por términos de agentes clásicos ("AI agent*", "autonomous agent*", "multi-agent system*"), sin ningún término de GenAI, LLM, ChatGPT, GPT, RAG o agentic AI, de pertinencia discutible para IA generativa y agéntica (la decisión de incluirlos depende del alcance de la revisión).

**Changes:** propuesta (**no ejecutada**) para la cadena 03. Revisión (2026-11-03): la versión original de este campo decía "ninguna; la cadena final es la 02" y declaraba convergencia. Se retiró por indicación del usuario, que señaló que si se incluye ChatGPT deben incluirse también Claude y otros modelos; la objeción es válida por el mismo mecanismo (ver Evaluation). La cadena 03 es la 02 más nombres de modelos y proveedores de LLM con uso verificado en el corpus; no se elimina ningún término.

```sql
TITLE-ABS-KEY (
  "generative AI" OR
  "generative artificial intelligence" OR
  GenAI OR
  "large language model*" OR
  LLM OR LLMs OR
  "foundation model*" OR
  "agentic AI" OR
  "agentic artificial intelligence" OR
  "AI agent*" OR
  "autonomous agent*" OR
  "multi-agent system*" OR
  "multiagent system*" OR
  ChatGPT OR
  "GPT*" OR
  "retrieval-augmented generation" OR
  Claude OR
  Gemini OR
  "Llama*" OR
  DeepSeek OR
  Mistral OR
  Qwen OR
  Copilot OR
  OpenAI OR
  Anthropic
)
AND
TITLE-ABS-KEY (
  "learning analytics" OR
  "teaching analytics" OR
  "educational data mining" OR
  "academic analytics"
)
```

**Rationale:**

- Revisión (2026-11-03): la convergencia declarada originalmente en esta iteración se retira. Se apoyaba en un argumento inválido sobre los nombres de modelos (ver Evaluation y la revisión en la Iteration 1). La cadena 02 sigue siendo una cadena ejecutada y validada, pero no se considera final.
- Para la cadena 03: se agregan solo nombres con uso confirmado como modelo o proveedor de LLM en el corpus y al menos 3 registros (Gemini 20, Llama 19, Claude 13, OpenAI 11, DeepSeek 10, Copilot 10, Qwen 8, Mistral 3, Anthropic 3). Quedan fuera los nombres con 1 o 2 registros (p. ej., Bard, Gemma, Grok, Kimi, ERNIE) por no tener evidencia suficiente para justificar su inclusión y por ambigüedad (Grok, Bard). Gemini, Llama, Claude y Mistral son homónimos de otras palabras, pero el bloque 2 (AND) limita el ruido; el CSV permitirá medirlo. Se espera que la cadena 03, por ser un superconjunto de la 02, no pierda ningún registro (0 perdidos; si faltara alguno de los 936 EID, se tratará como inconsistencia de la exportación). No se verificó cómo Scopus procesa el comodín de "Llama*".
- Convergencia operativa (valoración original, conservada): el conjunto es estable (0 pérdidas inesperadas, predicción de pérdidas confirmada), el rendimiento marginal cayó de 48 registros (5,4 %) a 14 (1,5 %), y de los 14 solo 8 son claramente pertinentes (alrededor de 0,9 % de la base). Los conceptos principales de ambos bloques están cubiertos y no hay términos o enfoques claramente omitidos con evidencia en los CSV.
- Esto es convergencia operativa, no una demostración de exhaustividad: los CSV solo contienen documentos ya recuperados, y no pueden mostrar los que la cadena sigue sin ver. (Revisión: la frase original añadía que las expansiones con otros nombres de modelos no tenían evidencia a favor; esa conclusión era errónea, ver arriba.)
- La cadena final se conserva sin filtros por tipo de documento, según las restricciones del procedimiento.

**Validation Results:**

- Registros: 936; EID únicos: 936; duplicados por EID: 0; DOI presentes: 786 (únicos: 786); sin DOI: 150; sin resumen: 2. Las columnas son idénticas a las de las iteraciones anteriores.
- Respecto a la iteración 1 (por EID): nuevos 14; conservados 922; perdidos 11. Los 11 perdidos coinciden exactamente con los 11 predichos.
- Respecto a la iteración 0 (por EID): nuevos 51; conservados 885; perdidos 0.
- Perfil: 875 de 936 son de 2024 o posterior; 777 de 2025 o posterior; 31 de 2022 o anterior. Tipos: 484 conference paper, 268 article, 75 conference review, 43 review, 43 book chapter, 14 editorial, 5 book, 3 note, 1 data paper.
- Aproximación por expresiones regulares sobre título, resumen y palabras clave (guiones como espacios); 4 registros no satisfacen literalmente el bloque 2 con esa aproximación (Scopus los recuperó por un procesamiento que no se reprodujo). La pertinencia se evaluó por lectura de títulos y contextos del resumen, sin validación con dos revisores.

**Convergence Status:** `continue` (revisado el 2026-11-03; el valor original era `converged`)

<!-- Append subsequent iterations below. Preserve previous iterations. -->


