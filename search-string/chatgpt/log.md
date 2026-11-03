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



## Iteration 1 — Scopus export of search 01

**Timestamp:** 2026-11-03 (analysis date; export date not independently verified)

### Search String

Executed query 01:

```sql
TITLE-ABS-KEY ( "generative AI" OR "generative artificial intelligence" OR GenAI OR "large language model*" OR LLM OR LLMs OR "foundation model*" OR "agentic AI" OR "agentic artificial intelligence" OR "AI agent*" OR "autonomous agent*" OR "multi-agent system*" OR "multiagent system*" ) AND TITLE-ABS-KEY ( "learning analytics" OR "teaching analytics" OR "educational data mining" OR "academic analytics" ) AND TITLE-ABS-KEY ( teach* OR learn* OR student* OR instructor* OR pedagog* OR curricul* OR assess* OR feedback )
```

### Evaluation

- Input: `chatgp-01.csv` (882 records, 22 columns).
- Compared by Scopus EID to query 00 CSV: **882 retained, 3 lost, 0 new** (99.66% retention).
- All 882 records have abstracts; no duplicate nonempty DOIs detected.
- Literal phrase occurrences in title, abstract, or author keywords: learning analytics 775; educational data mining 121; data analytics 17; business analytics 1; generative AI 389; large language model 390; agentic 27. These are overlapping text matches, not eligibility classifications.
- The additional education block did not materially increase specificity as measured by record count (885 → 882), and its effect on relevance has not been established.

### Changes

**Proposed next search string 02 (not executed):** remove the third education block and expand GenAI terminology with ChatGPT, GPT-3, GPT-4, generative agents, and retrieval-augmented generation.

```sql
TITLE-ABS-KEY ( "generative AI" OR "generative artificial intelligence" OR GenAI OR "large language model*" OR LLM OR LLMs OR "foundation model*" OR "agentic AI" OR "agentic artificial intelligence" OR "AI agent*" OR "autonomous agent*" OR "multi-agent system*" OR "multiagent system*" OR ChatGPT OR "GPT-3" OR "GPT-4" OR "generative agent*" OR "retrieval augmented generation" OR "retrieval-augmented generation" ) AND TITLE-ABS-KEY ( "learning analytics" OR "teaching analytics" OR "educational data mining" OR "academic analytics" )
```

### Rationale

The education block removed only three records and yielded no new records. Broadening GenAI terminology while retaining the original domain block is a test of additional retrieval. Newly added terms are candidates for evaluation, not proof of greater recall; some (e.g. retrieval-augmented generation) may introduce non-generative or off-topic records.

### Validation Results

- Query 00: 885 records; query 01: 882 records.
- Set comparison (EID): 0 new; 3 excluded; 882 shared.
- Three excluded titles: *AutoMind: Automated Insight Discovery via Multi-Agent Navigation*; *User Profile Generation Framework Based on Large Language Model Enhanced by Dynamic and Static Knowledge Graphs*; *Comparing Human Role-Players and LLM-Simulated Clients in Online Counselling Training: An Analysis of Counselling Pat...* (title truncated here; full title remains in the source CSV).
- Manual relevance assessment, seed-paper recall, and query 02 retrieval are pending.

### Convergence Status

`continue` — **NO, not converged**. Execute query 02 in Scopus and supply its CSV for evaluation.
