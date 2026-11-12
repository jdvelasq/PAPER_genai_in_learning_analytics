## Iteración 1

### Cadena inicial
```text
TITLE-ABS-KEY(
  (
    "learning analytic*" OR
    "teaching analytic*" OR
    "educational data mining"
  )
  AND
  (
    "generative artificial intelligence" OR
    "generative ai" OR
    "genai" OR
    "gen-ai" OR
    "agentic artificial intelligence" OR
    "agentic ai" OR
    "ai agent*" OR
    "autonomous agent*" OR
    "multi-agent*" OR
    "large language model*" OR
    "llm*" OR
    "foundation model*" OR
    "chatgpt" OR
    "gpt-4" OR
    "gpt-4o" OR
    "gpt-3.5" OR
    "claude" OR
    "anthropic" OR
    "gemini" OR
    "google bard" OR
    "bard" OR
    "copilot" OR
    "microsoft copilot" OR
    "llama" OR
    "mistral" OR
    "deepseek" OR
    "qwen" OR
    "grok"
  )
)
```

## Iteración 2

- Artículos recuperados: 935
- Estado: No converge
- Explicación: Se analizaron título, abstract, author keywords e index keywords de los 935 registros de 01.csv. Para maximizar exhaustividad, se incorporan al bloque analítico variantes consolidadas (educational analytic*, academic analytic*, learner analytic*, student analytic* y knowledge tracing). Al bloque de GenAI y agentes se agregan chatbot*, conversational agent*, conversational ai, intelligent agent*, pedagogical agent*, ai tutor*, retrieval-augmented generation y prompt engineering. Se añade xai junto a grok.

### Nueva cadena sugerida
```text
TITLE-ABS-KEY(
  (
    "learning analytic*" OR
    "teaching analytic*" OR
    "educational analytic*" OR
    "academic analytic*" OR
    "learner analytic*" OR
    "student analytic*" OR
    "educational data mining" OR
    "knowledge tracing"
  )
  AND
  (
    "generative artificial intelligence" OR
    "generative ai" OR
    "genai" OR
    "gen-ai" OR
    "agentic artificial intelligence" OR
    "agentic ai" OR
    "ai agent*" OR
    "autonomous agent*" OR
    "intelligent agent*" OR
    "pedagogical agent*" OR
    "ai tutor*" OR
    "multi-agent*" OR
    "large language model*" OR
    "llm*" OR
    "foundation model*" OR
    "chatgpt" OR
    "gpt-4" OR
    "gpt-4o" OR
    "gpt-3.5" OR
    "chatbot*" OR
    "conversational agent*" OR
    "conversational ai" OR
    "retrieval-augmented generation" OR
    "prompt engineering" OR
    "claude" OR
    "anthropic" OR
    "gemini" OR
    "google bard" OR
    "bard" OR
    "copilot" OR
    "microsoft copilot" OR
    "llama" OR
    "mistral" OR
    "deepseek" OR
    "qwen" OR
    "grok" OR
    "xai"
  )
)
```

## Iteración 3

- Artículos recuperados: 1540
- Estado: No converge
- Explicación: Se analizaron título, abstract, author keywords e index keywords de los 1,540 registros de 02.csv. Para maximizar exhaustividad, en el bloque analítico se incorporan learner model*, student model*, learning trace* y educational process mining. En el bloque de GenAI y agentes se incorporan multiagent*, virtual assistant*, teaching assistant*, generative model*, gpt-3 y gpt-5. La cadena no converge al detectarse términos formativos y de modelado adicionales con presencia empírica.

### Nueva cadena sugerida
```text
TITLE-ABS-KEY(
  (
    "learning analytic*" OR
    "teaching analytic*" OR
    "educational analytic*" OR
    "academic analytic*" OR
    "learner analytic*" OR
    "student analytic*" OR
    "educational data mining" OR
    "knowledge tracing" OR
    "learner model*" OR
    "student model*" OR
    "learning trace*" OR
    "educational process mining"
  )
  AND
  (
    "generative artificial intelligence" OR
    "generative ai" OR
    "genai" OR
    "gen-ai" OR
    "agentic artificial intelligence" OR
    "agentic ai" OR
    "ai agent*" OR
    "autonomous agent*" OR
    "intelligent agent*" OR
    "pedagogical agent*" OR
    "ai tutor*" OR
    "virtual assistant*" OR
    "teaching assistant*" OR
    "multi-agent*" OR
    "multiagent*" OR
    "generative model*" OR
    "large language model*" OR
    "llm*" OR
    "foundation model*" OR
    "chatgpt" OR
    "gpt-3" OR
    "gpt-3.5" OR
    "gpt-4" OR
    "gpt-4o" OR
    "gpt-5" OR
    "chatbot*" OR
    "conversational agent*" OR
    "conversational ai" OR
    "retrieval-augmented generation" OR
    "prompt engineering" OR
    "claude" OR
    "anthropic" OR
    "gemini" OR
    "google bard" OR
    "bard" OR
    "copilot" OR
    "microsoft copilot" OR
    "llama" OR
    "mistral" OR
    "deepseek" OR
    "qwen" OR
    "grok" OR
    "xai"
  )
)
```

## Iteración 4

- Artículos recuperados: 2616
- Estado: Converge
- Explicación: Se analizaron título, abstract, author keywords e index keywords de los 2,616 registros de 03.csv. La cadena recupera exhaustivamente las familias conceptuales de analíticas del aprendizaje (LA/TA, EDM, knowledge tracing, modelado y trazas) y de IA generativa y agéntica (LLMs, agentes, asistentes, RAG, prompt engineering y proveedores simétricos). No se identifican nuevos términos o variantes cuya inclusión aumente materialmente la recuperación exhaustiva sin comprometer la especificidad del tema. Se declara la convergencia.

### Cadena final seleccionada
```text
TITLE-ABS-KEY(
  (
    "learning analytic*" OR
    "teaching analytic*" OR
    "educational analytic*" OR
    "academic analytic*" OR
    "learner analytic*" OR
    "student analytic*" OR
    "educational data mining" OR
    "knowledge tracing" OR
    "learner model*" OR
    "student model*" OR
    "learning trace*" OR
    "educational process mining"
  )
  AND
  (
    "generative artificial intelligence" OR
    "generative ai" OR
    "genai" OR
    "gen-ai" OR
    "agentic artificial intelligence" OR
    "agentic ai" OR
    "ai agent*" OR
    "autonomous agent*" OR
    "intelligent agent*" OR
    "pedagogical agent*" OR
    "ai tutor*" OR
    "virtual assistant*" OR
    "teaching assistant*" OR
    "multi-agent*" OR
    "multiagent*" OR
    "generative model*" OR
    "large language model*" OR
    "llm*" OR
    "foundation model*" OR
    "chatgpt" OR
    "gpt-3" OR
    "gpt-3.5" OR
    "gpt-4" OR
    "gpt-4o" OR
    "gpt-5" OR
    "chatbot*" OR
    "conversational agent*" OR
    "conversational ai" OR
    "retrieval-augmented generation" OR
    "prompt engineering" OR
    "claude" OR
    "anthropic" OR
    "gemini" OR
    "google bard" OR
    "bard" OR
    "copilot" OR
    "microsoft copilot" OR
    "llama" OR
    "mistral" OR
    "deepseek" OR
    "qwen" OR
    "grok" OR
    "xai"
  )
)
```
