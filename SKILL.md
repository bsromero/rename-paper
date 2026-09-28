---
name: rename-paper
description: Rename research papers, reports, working papers, and academic PDFs to the user's citation-style filename "Title — Author (Year).pdf". Use whenever the user asks to rename a paper, study, report, or evidence document, or to tidy up downloaded PDFs with messy names like "Salaried-Labor-Costs-...- (1).pdf" or "articles-12345_doc.pdf".
---

# Rename paper

Rename academic/research PDFs to this exact format:

```
Title — Authors (Year).pdf
```

Examples:
- `15 Years of Research on U.S. Employment and the Minimum Wage — Belman & Wolfson (2016).pdf`
- `Salaried Labor Costs in Latin America and the Caribbean: A Ten-Year Update — Alaimo et al. (2026).pdf`
- `The Effect of Minimum Wages on Low-Wage Jobs — Cengiz et al. (2019).pdf`

## Rules

- **Title**: the full title as printed on the document, including subtitle. Keep the colon between title and subtitle. Use the document's own capitalization. Fix artifacts from the download name (hyphens-for-spaces, `---`, trailing ` (1)`, stray spaces like "Ten - Year" → "Ten-Year").
- **Separator**: a spaced em dash ` — ` (U+2014), never a hyphen.
- **Authors**: last names only, no first names or initials.
  - 1 author: `Card`
  - 2 authors: `Belman & Wolfson`
  - 3 or more: `Alaimo et al.`
  - Keep accents and particles as printed (`Pérez`, `de la Torre`).
  - If the author is an institution with no personal authors, use its short name (`OECD`, `IDB`, `Banco Central de Chile`).
- **Year**: publication year of this version, in parentheses. Prefer the date printed on the cover/title page over PDF metadata dates. For working papers later published in a journal, use the year of the version in hand.
- Keep the original extension.
- Characters macOS/OneDrive reject: replace `/` with `-`; colons are fine on macOS but OneDrive syncs them — they have worked in the user's OneDrive so far, keep them.

## Workflow

1. Extract text from the first pages:
   ```bash
   python3 ~/.claude/skills/rename-paper/scripts/extract_front.py "<file.pdf>"
   ```
   It prints the first ~3 pages of text plus any PDF metadata title/author. `pdftotext`/`pdfinfo`/poppler are **not** installed on this machine and Homebrew isn't on PATH; pdfminer is the tool that works.
2. Identify title, authors, and year from the cover/title page. Do not rely on the download filename or XMP dates alone — they're often wrong (e.g. XMP said 2024, cover said February 2026).
3. If the text layer is empty (scanned PDF) and nothing can be determined, tell the user what you found and ask rather than guessing authors.
4. Rename with `mv`, quoting paths (they contain spaces and accents). Check the target name doesn't already exist first so nothing is overwritten.
5. Report the new name in one line. For several files, show an old → new list.

For non-paper documents with a periodic series (e.g. monthly government reports), this format doesn't apply — ask the user what pattern they want.
