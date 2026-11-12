## Iteración 1

### Cadena inicial
```text
TITLE-ABS-KEY(
    (
        "learning analytics" OR "teaching analytics" OR "educational analytics"
        OR "learner analytics" OR "student analytics" OR "academic analytics"
        OR "educational data mining"
    )
    AND
    (
        "generative ai" OR "generative artificial intelligence" OR "genai"
        OR "gen ai" OR "agentic ai" OR "agentic artificial intelligence"
        OR "ai agent*" OR "large language model*" OR "llm*"
        OR "foundation model*" OR "chatgpt" OR "gpt*"
        OR "claude" OR "anthropic" OR "gemini" OR "bard" OR "grok" OR "xai"
        OR "copilot" OR "llama" OR "mistral" OR "deepseek" OR "qwen"
    )
)
```
## Iteración 2

- Artículos recuperados (01.csv): 1108
- Estado: No converge
- Explicación: Se revisaron título, abstract y keywords de 01.csv. Se encontraron términos relevantes ausentes: chatbot (78 registros en título/abstract), conversational agent (13), multi-agent (32) y retrieval-augmented generation (13 author keywords). Se añaden. Se cambia learning analytics por learning analytic* porque las index keywords usan "learning analytic" (325 registros).

### Nueva cadena sugerida
```text
TITLE-ABS-KEY(
    (
        "learning analytic*" OR "teaching analytics" OR "educational analytics"
        OR "learner analytics" OR "student analytics" OR "academic analytics"
        OR "educational data mining"
    )
    AND
    (
        "generative ai" OR "generative artificial intelligence" OR "genai"
        OR "gen ai" OR "agentic ai" OR "agentic artificial intelligence"
        OR "ai agent*" OR "multi-agent system*" OR "large language model*"
        OR "llm*" OR "foundation model*" OR "chatgpt" OR "gpt*" OR "chatbot*"
        OR "conversational agent*" OR "retrieval-augmented generation"
        OR "claude" OR "anthropic" OR "gemini" OR "bard" OR "grok" OR "xai"
        OR "copilot" OR "llama" OR "mistral" OR "deepseek" OR "qwen"
    )
)
```
## Iteración 3

- Artículos recuperados (02.csv): 1281
- Estado: No converge
- Explicación: Se revisaron título, abstract y keywords de 02.csv. Se añaden términos de agentes y asistentes con volumen real en título/abstract: "ai tutor" (17), "teaching assistant" (9), "intelligent agent" (9), "virtual assistant" (4) y "multi-agent" (63). Se añade "conversational ai" y "prompt engineering" (la palabra "prompt" aparece en 149 registros). Se usa "multi-agent*" para cubrir "multi-agent" sin sufijo. No converge porque aún hay términos nuevos con volumen.

### Nueva cadena sugerida
```text
TITLE-ABS-KEY(
    (
        "learning analytic*" OR "teaching analytics" OR "educational analytics"
        OR "learner analytics" OR "student analytics" OR "academic analytics"
        OR "educational data mining"
    )
    AND
    (
        "generative ai" OR "generative artificial intelligence" OR "genai"
        OR "gen ai" OR "agentic ai" OR "agentic artificial intelligence"
        OR "ai agent*" OR "intelligent agent*" OR "virtual assistant*"
        OR "teaching assistant*" OR "ai tutor*" OR "multi-agent*"
        OR "large language model*" OR "llm*" OR "foundation model*"
        OR "chatgpt" OR "gpt*" OR "chatbot*" OR "conversational agent*"
        OR "conversational ai" OR "retrieval-augmented generation"
        OR "prompt engineering"
        OR "claude" OR "anthropic" OR "gemini" OR "bard" OR "grok" OR "xai"
        OR "copilot" OR "llama" OR "mistral" OR "deepseek" OR "qwen"
    )
)
```
## Iteración 4

- Artículos recuperados (03.csv): 1349
- Estado: Converge
- Explicación: Se revisaron título, abstract y keywords de 03.csv. La cadena de la iteración 3 cubre 1343 de 1349 registros. Los 6 restantes no se recuperan con términos nuevos razonables: "agentic", "assistant" y "tutor" no añaden registros; "agent" añade 1 y "generative" añade 3, pero son términos demasiado amplios. No se añaden cambios.

### Cadena final seleccionada
```text
TITLE-ABS-KEY(
    (
        "learning analytic*" OR "teaching analytics" OR "educational analytics"
        OR "learner analytics" OR "student analytics" OR "academic analytics"
        OR "educational data mining"
    )
    AND
    (
        "generative ai" OR "generative artificial intelligence" OR "genai"
        OR "gen ai" OR "agentic ai" OR "agentic artificial intelligence"
        OR "ai agent*" OR "intelligent agent*" OR "virtual assistant*"
        OR "teaching assistant*" OR "ai tutor*" OR "multi-agent*"
        OR "large language model*" OR "llm*" OR "foundation model*"
        OR "chatgpt" OR "gpt*" OR "chatbot*" OR "conversational agent*"
        OR "conversational ai" OR "retrieval-augmented generation"
        OR "prompt engineering"
        OR "claude" OR "anthropic" OR "gemini" OR "bard" OR "grok" OR "xai"
        OR "copilot" OR "llama" OR "mistral" OR "deepseek" OR "qwen"
    )
)
```
