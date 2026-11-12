# Final search string protocol

## Purpose

Create one final Scopus search string that consolidates the final search
strings produced independently by Claude, Codex, and Gemini.

## Required input

Read and analyze the final search strings in all of these files:

```text
step-0-search-string/claude/log.md
step-0-search-string/codex/log.md
step-0-search-string/gemini/log.md
```

Locate the search string labelled `Cadena final seleccionada` in each log. Do
not use an initial or intermediate iteration when a final selected string is
available.

## Process

1. Compare the three final strings by conceptual block.
2. Consolidate their synonyms, spelling variants, acronyms, technology names,
   and other relevant terms into one final Scopus search string.
3. Start from the union of all terms in the three final strings. A term must be
   retained unless it is an exact duplicate or is demonstrably covered by a
   broader term in the final Scopus syntax.
4. Do not remove a term because it is merely related to another term.
   For example, `conversational ai` does not cover `conversational agent*`, and
   an agent-related expression does not cover `ai tutor*`, `teaching
   assistant*`, `virtual assistant*`, `retrieval-augmented generation`, or
   `prompt engineering`.
5. Before writing the output, verify coverage term by term against every final
   source string. For each source term, confirm that it is either present in
   the final string or covered by a specific retained expression. If that
   coverage cannot be demonstrated, add the source term to the final string.
6. Combine synonyms with `OR` and distinct concepts with `AND`. Preserve valid
   Scopus syntax, preferably using `TITLE-ABS-KEY(...)`.
7. Do not invent Scopus results, add arbitrary filters, or discard relevant
   coverage merely to make the query shorter.

## Output

Write only the final search string to:

```text
step-0-search-string/final-search-string.txt
```

The output file must contain no title, Markdown fence, explanation, or other
text. Format the string across multiple lines so every line is at most 80
characters wide, including indentation. Keep logical indentation and place
Boolean operators consistently so that the query remains easy to read and can
be copied directly into Scopus.
