# Selection criteria

## Purpose and scope

These criteria select the records that will inform a systematic mapping of
Generative Artificial Intelligence (GenAI) and Agentic Artificial Intelligence
(Agentic AI) in Learning Analytics (LA) and Teaching Analytics (TA). They are
derived from the review objective and RQ1–RQ4 in
[`research-questions.md`](research-questions.md), and align the resulting
corpus with the educational-technology focus of IEEE-RITA described in
[`aims-and-scope.md`](aims-and-scope.md).

The unit of selection is a bibliographic record. Decisions are based on title,
abstract, author keywords, and index keywords; full texts are not reviewed in
this protocol. Therefore, a record is included only when those fields provide
enough evidence to apply the criteria below.

## Operational constraints applied before screening

The following transparent constraints are applied before substantive screening:

- Document type: Article, Book chapter, Conference paper, Conference review,
  or Review.
- Language of original document: English.
- Abstract: present and longer than 80 characters.

Records failing any of these constraints are recorded as removed before
screening, not as exclusions after substantive screening.

## Inclusion criteria

A record is included only when it meets **all** of the following criteria.

| ID | Criterion | Operational decision rule |
| --- | --- | --- |
| I1 | Educational relevance | The study concerns a learning, teaching, assessment, feedback, curriculum, learner-support, or instructor-support context, process, or intervention. |
| I2 | GenAI or Agentic AI is substantive | The study investigates, designs, evaluates, applies, or analyses a generative model, large language model, generative AI system, AI agent, or multi-agent system. A passing reference to such technology is insufficient. |
| I3 | Explicit LA or TA connection | The technology is used for, or its effects are examined in relation to, the collection, analysis, interpretation, communication, or use of learner/teacher data to understand, support, or improve learning or teaching. This includes analytics-informed feedback, dashboards, prediction, modelling, process/discourse analysis, or instructional decision support. |
| I4 | Relevance to at least one research question | The record contains information that can contribute to at least one of the review questions: research themes/evolution; technological functions; data, processes, decisions, interventions, or stakeholders; or methods, validation, evidence, and limitations. |
| I5 | Sufficient metadata evidence | The title, abstract, and available keywords allow I1–I4 to be verified without inferring information absent from the record. |

No restriction is imposed on publication year, educational level, country or
region, discipline, study design, or reported direction of findings. Engineering
and computing education are especially relevant to IEEE-RITA, but are not made
an exclusive condition because the review questions address LA and TA across
educational settings.

## Exclusion criteria

A record is excluded when it meets any criterion below.

| ID | Criterion | Operational decision rule |
| --- | --- | --- |
| E1 | Not an educational study | The record concerns a non-educational domain and does not analyse or support a learning or teaching process. |
| E2 | GenAI/Agentic AI is absent or incidental | The study concerns only non-generative AI, conventional analytics, or another technology; or it mentions GenAI/Agentic AI without making it a substantive object of study, design, use, or evaluation. |
| E3 | No LA or TA connection | The study examines GenAI/Agentic AI in education but does not address learner/teacher data, an analytic process, analytics-informed feedback or decision-making, or an LA/TA outcome. Generic use, perceptions, adoption, or performance studies alone do not satisfy this criterion. |
| E4 | Outside the review questions | The available metadata cannot contribute evidence to RQ1, RQ2, RQ3, or RQ4. |
| E5 | Insufficient information | The title, abstract, and keywords do not permit a defensible decision on I1–I4. Because full texts are not reviewed, ambiguous records are excluded and recorded with this reason. |

## Decision procedure and audit trail

1. Apply the operational constraints to `identified.csv` to produce
   `screened.csv`.
2. Assess each screened record against I1–I5 using title, abstract, author
   keywords, and index keywords.
3. Include a record only if all inclusion criteria are met and no exclusion
   criterion applies.
4. For every excluded record, record one primary exclusion reason (E1–E5).
   When more than one applies, use the first applicable reason in numerical
   order to keep reporting mutually exclusive.
5. Retain the decision, primary reason, and reviewer notes in the selection
   dataset so the PRISMA counts and the final corpus can be reproduced.

The resulting included set is suitable for the mapping analysis, while the
absence of full-text assessment must be stated as a methodological limitation
in the manuscript.
