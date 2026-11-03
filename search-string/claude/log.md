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

<!-- Append subsequent iterations below. Preserve previous iterations. -->
