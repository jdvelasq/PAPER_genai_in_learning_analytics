## Iteración 1

### Cadena inicial
```text
TITLE-ABS-KEY(
  (
    "generative artificial intelligence" OR "generative ai" OR genai OR
    "generative model*" OR "generative language model*" OR
    "large language model*" OR llm OR llms OR "foundation model*" OR
    "generative pretrained transformer*" OR "ai-generated" OR
    "ai generated" OR "generative agent*" OR "agentic ai" OR
    "agentic artificial intelligence" OR "ai agent*" OR
    "artificial intelligence agent*" OR "autonomous agent*" OR
    "intelligent agent*" OR "pedagogical agent*" OR
    "educational agent*" OR "multi-agent system*" OR
    "multiagent system*" OR "autonomous ai" OR "conversational ai" OR
    chatbot* OR chatgpt OR claude OR anthropic OR grok OR xai OR
    gemini OR bard OR copilot OR "microsoft copilot" OR llama OR
    mistral OR deepseek OR qwen OR gpt-3 OR gpt-4 OR gpt-5
  )
  AND
  (
    "learning analytic*" OR "teaching analytic*" OR
    "learning and teaching analytic*" OR "teaching and learning analytic*" OR
    "educational analytic*" OR "education analytic*" OR
    "academic analytic*" OR "student analytic*" OR
    "learner analytic*" OR "teacher analytic*" OR
    "instructor analytic*" OR "classroom analytic*" OR
    "instructional analytic*" OR "assessment analytic*" OR
    "feedback analytic*" OR "discourse analytic*" OR
    "multimodal learning analytic*" OR "learning data analytic*" OR
    "student success analytic*" OR "learning intelligence" OR
    "teaching intelligence" OR "learner model*" OR
    "student model*" OR "learner modeling" OR "student modeling" OR
    "knowledge tracing" OR "educational data science" OR
    "learning engineering" OR "education data mining" OR
    "educational data mining" OR EDM
  )
)
```

El resultado quedo almacenado en el archivo `01.csv`.

## Iteración 2

- Artículos recuperados: 2,719
- Estado: No converge
- Explicación: La exportación contiene título, abstract, author keywords e index keywords. La revisión identifica variantes específicas de Learning Analytics ausentes en la cadena inicial: learning analytics dashboards, learning analytics systems, learning analytics platforms, learning traces y educational process mining. No se incorporan términos genéricos como student data o educational data porque ampliarían innecesariamente la recuperación.

### Nueva cadena sugerida
```text
TITLE-ABS-KEY(
  (
    "generative artificial intelligence" OR "generative ai" OR genai OR
    "generative model*" OR "generative language model*" OR
    "large language model*" OR llm OR llms OR "foundation model*" OR
    "generative pretrained transformer*" OR "ai-generated" OR
    "ai generated" OR "generative agent*" OR "agentic ai" OR
    "agentic artificial intelligence" OR "ai agent*" OR
    "artificial intelligence agent*" OR "autonomous agent*" OR
    "intelligent agent*" OR "pedagogical agent*" OR
    "educational agent*" OR "multi-agent system*" OR
    "multiagent system*" OR "autonomous ai" OR "conversational ai" OR
    chatbot* OR chatgpt OR claude OR anthropic OR grok OR xai OR
    gemini OR bard OR copilot OR "microsoft copilot" OR llama OR
    mistral OR deepseek OR qwen OR gpt-3 OR gpt-4 OR gpt-5
  )
  AND
  (
    "learning analytic*" OR "teaching analytic*" OR
    "learning and teaching analytic*" OR "teaching and learning analytic*" OR
    "educational analytic*" OR "education analytic*" OR
    "academic analytic*" OR "student analytic*" OR
    "learner analytic*" OR "teacher analytic*" OR
    "instructor analytic*" OR "classroom analytic*" OR
    "instructional analytic*" OR "assessment analytic*" OR
    "feedback analytic*" OR "discourse analytic*" OR
    "multimodal learning analytic*" OR "learning data analytic*" OR
    "student success analytic*" OR "learning intelligence" OR
    "teaching intelligence" OR "learner model*" OR
    "student model*" OR "learner modeling" OR "student modeling" OR
    "knowledge tracing" OR "learning analytics dashboard*" OR
    "learning analytics system*" OR "learning analytics platform*" OR
    "learning trace*" OR "educational process mining" OR
    "education data mining" OR "educational data mining" OR edm
  )
)
```


