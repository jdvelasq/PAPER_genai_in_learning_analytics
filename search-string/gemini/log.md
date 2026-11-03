# Search Strategy Refinement Log

## Iteration 0

**Timestamp:** 2026-11-03 09:30:00 -05:00

**Search String:**
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
- **Volume & Deduplication:** Retrieved 885 records from Scopus (`scopus-0.csv`). No duplicates were identified by Scopus EID (885 unique EIDs) or DOI (749 non-empty DOIs, all unique).
- **Temporal Distribution:** Publications span 2005 to 2027 (indexed advance publications). Pre-2023 accounts for 31 records (3.5%), 2023 has 22 (2.5%), 2024 has 87 (9.8%), 2025 has 218 (24.6%), 2026 has 488 (55.1%), and 2027 has 39 (4.4%).
- **Document Types:** Conference paper: 460 (52.0%), Article: 253 (28.6%), Conference review: 67 (7.6%), Review: 41 (4.6%), Book chapter: 41 (4.6%), Editorial: 14 (1.6%), Book: 5 (0.6%), Note: 3 (0.3%), Data paper: 1 (0.1%).
- **Terminology Coverage - AI Dimension:**
  - High-frequency GenAI terms: "generative ai" (390; 44.1%), "large language models" (325; 36.7%), "large language model" (257; 29.0%), "llm" (234; 26.4%), "generative artificial intelligence" (219; 24.7%), "llms" (210; 23.7%), "genai" (164; 18.5%).
  - Agentic AI terms: "multi-agent systems" (24; 2.7%), "agentic ai" (19; 2.1%), "multi-agent system" (18; 2.0%), "multiagent systems" (18; 2.0%), "autonomous agents" (15; 1.7%), "ai agents" (12; 1.4%), "ai agent" (9; 1.0%), "agentic artificial intelligence" (6; 0.7%), "foundation models" (5; 0.6%), "autonomous agent" (1; 0.1%).
- **Terminology Coverage - Analytics Dimension:**
  - "learning analytics": 775 (87.6%)
  - "educational data mining": 124 (14.0%)
  - "teaching analytics": 8 (0.9%)
  - "academic analytics": 4 (0.5%)
- **Identified Noise / False Positives:**
  - 29 records matched solely classic multi-agent system or autonomous agent terms (e.g., pre-2022 distributed AI, rule-based multi-agent systems, workshop proceedings) without any reference to modern Generative AI or Agentic AI constructs.
- **Identified Gaps / Potential Omissions:**
  - *Generative AI dimension:* Widely used model designations such as `ChatGPT` (present in 90 records of the baseline set, but missing from the query string itself; any paper using ChatGPT in learning analytics without the generic string "generative AI" or "large language model" is omitted) and formal terms like `"generative pre-trained transformer*"` / `"generative pretrained transformer*"`.
  - *Agentic AI dimension:* Crucial modern constructs such as `"generative agent*"` (bridging GenAI and agentic architectures) and `"agentic workflow*"` / `"agentic system*"` are absent.
  - *Analytics dimension:* The teaching facet is notably underrepresented ("teaching analytics" = 8 records). Key complementary terms such as `"teacher analytics"` and `"classroom analytics"` are missing.

**Changes:**
Proposed Query 01 expands both the GenAI/Agentic AI and the Analytics facets incrementally:
1. Add leading model families (`ChatGPT`, `"GPT-4*"`, `Claude`, `Gemini`, `LLaMA`) to capture model-specific comparative and empirical literature while avoiding commercial provider bias.
2. Add `"generative pre-trained transformer*"` and `"generative pretrained transformer*"` to capture formal terminology.
3. Add `"generative agent*"` and `"agentic system*"` and `"agentic workflow*"` to enhance Agentic AI recall.
4. Add `"teacher analytics"` and `"classroom analytics"` to strengthen the Teaching Analytics facet.

Proposed Query 01:
```sql
TITLE-ABS-KEY (
  "generative AI" OR
  "generative artificial intelligence" OR
  GenAI OR
  "large language model*" OR
  LLM OR LLMs OR
  "foundation model*" OR
  ChatGPT OR
  "GPT-4*" OR
  Claude OR
  Gemini OR
  LLaMA OR
  "generative pre-trained transformer*" OR
  "generative pretrained transformer*" OR
  "agentic AI" OR
  "agentic artificial intelligence" OR
  "agentic system*" OR
  "agentic workflow*" OR
  "generative agent*" OR
  "AI agent*" OR
  "autonomous agent*" OR
  "multi-agent system*" OR
  "multiagent system*"
)
AND
TITLE-ABS-KEY (
  "learning analytics" OR
  "teaching analytics" OR
  "teacher analytics" OR
  "classroom analytics" OR
  "educational data mining" OR
  "academic analytics"
)
```

**Rationale:**
The baseline search exhibits robust coverage of general GenAI concepts in learning analytics, but displays clear omissions: (1) Leading foundation models and applications (`ChatGPT`, `"GPT-4*"`, `Claude`, `Gemini`, `LLaMA`) are extensively evaluated in learning analytics research; including them avoids single-provider bias and ensures papers that evaluate specific models without employing generic terms like "large language model" are captured; (2) Agentic AI literature in education heavily employs `"generative agent*"`, `"agentic system*"`, and `"agentic workflow*"`; (3) Teaching Analytics is severely underrepresented (0.9%), and educator-oriented literature frequently uses `"teacher analytics"` or `"classroom analytics"`. An incremental addition allows direct measurement of recall expansion without conflating additions with premature exclusions.

**Validation Results:**
- Baseline iteration (Iteration 0).
- Total retrieved: 885 records.
- New records: 885.
- Retained records: N/A.
- Excluded records: N/A.

**Convergence Status:** `continue`
