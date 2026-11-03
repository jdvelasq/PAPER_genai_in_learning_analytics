# Search Strategy Refinement Log

## Iteration 0 — Initial Scopus export

**Timestamp:** 2026-11-03 (date of analysis; Scopus export date not verified)

### Search String

Executed Scopus query (provided by the user):

```sql
TITLE-ABS-KEY ( "generative AI" OR "generative artificial intelligence" OR GenAI OR "large language model*" OR LLM OR LLMs OR "foundation model*" OR "agentic AI" OR "agentic artificial intelligence" OR "AI agent*" OR "autonomous agent*" OR "multi-agent system*" OR "multiagent system*" ) AND TITLE-ABS-KEY ( "learning analytics" OR "teaching analytics" OR "educational data mining" OR "academic analytics" )
```

### Evaluation

- CSV: `chatgp-00(1).csv`; 885 records and 22 columns.
- Years: 2005–2027 (publication year metadata; 2027 includes future-dated records).
- Titles, abstracts and author keywords contain the literal phrase `learning analytics` in 775 records, `educational data mining` in 124, `data analytics` in 17, and `business analytics` in 1. Counts overlap and do not establish eligibility.
- The predominance of learning-analytics terminology warrants examining whether the query captures the *teaching and learning of Analytics* rather than primarily *analytics applied to education*.
- The executed query has two blocks (GenAI/agentic AI and learning/teaching/academic analytics); there is no explicit educational-process block. The query may retrieve studies applying GenAI to educational analytics without examining teaching or learning practices.

### Changes

**Proposed next search string (01; not executed):**

```sql
TITLE-ABS-KEY ( "generative AI" OR "generative artificial intelligence" OR GenAI OR "large language model*" OR LLM OR LLMs OR "foundation model*" OR "agentic AI" OR "agentic artificial intelligence" OR "AI agent*" OR "autonomous agent*" OR "multi-agent system*" OR "multiagent system*" ) AND TITLE-ABS-KEY ( "learning analytics" OR "teaching analytics" OR "educational data mining" OR "academic analytics" ) AND TITLE-ABS-KEY ( teach* OR learn* OR student* OR instructor* OR pedagog* OR curricul* OR assess* OR feedback )
```

Adds an educational-process block with teaching, learning, students, instructors, pedagogy, curricula, assessment and feedback terminology.

### Rationale

The original two-block query is now known. A third block is proposed to increase topical specificity; however, it could exclude relevant records that omit these words in indexed fields. The CSV alone cannot establish recall.

### Validation Results

- Retrieved records: **885**.
- Document types: 460 conference papers; 253 articles; 67 conference reviews; 41 reviews; 41 book chapters; 14 editorials; 5 books; 3 notes; 1 data paper.
- Missing abstracts: 0; missing author-keyword fields: 110.
- Duplicate nonempty DOI values: 0; duplicate EID values: 0.
- Independent seed-article recall: not evaluated.
- Relevance/precision: not evaluated.

### Convergence Status

`continue` — **not converged**. Execute proposed search 01 and provide its Scopus CSV to evaluate the change.

