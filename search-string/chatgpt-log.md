# ChatGPT — Scopus Search-String Iteration Log

**Research objective:** Develop and iteratively refine a Scopus search string for scholarly publications on Generative Artificial Intelligence (GenAI) and Agentic Artificial Intelligence (Agentic AI) in Teaching Analytics (TA) and Learning Analytics (LA).

**Database:** Scopus  
**LLM:** ChatGPT (GPT-6)  
**Logging language:** English

---

## Iteration 0

### 1. Iteration identification
- Iteration: 0 (baseline)
- Date: 2026-11-03
- LLM: ChatGPT (GPT-6)

### 2. Search string
The researcher confirmed that the **initial search string proposed by ChatGPT**, including wildcard asterisks, was executed in Scopus and produced the supplied CSV.

```text
TITLE-ABS-KEY(
  "generative AI" OR
  "generative artificial intelligence" OR
  GenAI OR
  "large language model*" OR
  LLM OR
  LLMs OR
  "foundation model*" OR
  "agentic AI" OR
  "agentic artificial intelligence" OR
  "AI agent*" OR
  "autonomous agent*" OR
  "multi-agent system*" OR
  "multiagent system*"
)
AND
TITLE-ABS-KEY(
  "learning analytics" OR
  "teaching analytics" OR
  "educational data mining" OR
  "academic analytics"
)
```

### 3. Scopus export
- Researcher-supplied file: `chatgp-00.csv`
- Database: Scopus
- Records: 885
- Export fields: 22, including title, abstract, author keywords, index keywords, year, DOI, document type, and EID.
- Exact executed query: confirmed by the researcher as the iteration 0 string shown above. Export date: not independently verified.

### 4. Retrieval statistics
- Total: **885** records.
- Publication years: **2005–2027** (as reported in the export).
- Before 2023: **31** (3.5%).
- 2023: **22**; 2024: **87**; 2025: **218**; 2026: **488**; 2027: **39**.
- Document types: conference papers **460**; articles **253**; conference reviews **67**; reviews **41**; book chapters **41**; other **23**.
- Missing abstracts: **0**; missing author keywords: **110**; duplicate EIDs: **0**.

### 5. Principal findings
- The search retrieves a predominantly recent corpus but also includes historical literature predating widespread contemporary GenAI use.
- Broad terms such as `"autonomous agent*"`, `"multi-agent system*"`, and `"educational data mining"` may contribute older or tangential records; this is a hypothesis requiring record-level relevance assessment.
- The export contains **39** records dated 2027, a future publication year relative to the logging date. Their publication stages should be checked before making date-based exclusions.
- Counts alone cannot establish precision or recall; title/abstract/keyword screening and a reference set of known relevant publications are needed.

### 6. Interpretation and refinement rationale
- Do not impose a publication-year cutoff solely to remove older records; first distinguish historical multi-agent educational systems from contemporary agentic AI research.
- Evaluate the contributions of `educational data mining` and `academic analytics` to the intended TA/LA scope.
- Check whether generic `LLM` and agent terminology causes off-topic retrieval.
- The researcher confirmed the exact baseline query; preserve its syntax unchanged for reproducibility.

### 7. Proposed next search string
**Pending record-level relevance screening.** The next candidate should retain both GenAI and Agentic AI, while assessing whether historical agent terms and adjacent analytics fields require narrowing. No untested revised query is recorded as an executed search.

### 8. Convergence status
**Not converged — baseline only.** One Scopus export has been analyzed; no iterative change in retrieval quality has yet been measured.

