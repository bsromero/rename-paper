# rename-paper

A Claude Code skill that renames research papers, reports, and academic PDFs to a consistent citation-style format.

## Format

```
Title — Authors (Year).pdf
```

### Examples

- `15 Years of Research on U.S. Employment and the Minimum Wage — Belman & Wolfson (2016).pdf`
- `Salaried Labor Costs in Latin America and the Caribbean: A Ten-Year Update — Alaimo et al. (2026).pdf`
- `The Effect of Minimum Wages on Low-Wage Jobs — Cengiz et al. (2019).pdf`

## Rules

- **Title**: Full title including subtitle (keep colons). Fix artifacts from download names (`Salaried-Labor-Costs-...- (1).pdf` → `Salaried Labor Costs...`).
- **Authors**: Last names only
  - 1 author: `Card`
  - 2 authors: `Belman & Wolfson`
  - 3+ authors: `Alaimo et al.`
- **Year**: Publication year from the document's cover/title page
- Separator: Spaced em dash ` — ` (U+2014)
- Keep accents and particles: `Pérez`, `de la Torre`, `van Reenen`

## Installation

Copy this directory into your Claude Code skills folder:

```bash
cp -r rename-paper ~/.claude/skills/
```

Or install via Claude Code `/skill-creator`.

## Usage

Invoke with `/rename-paper` and point Claude to the PDF file(s) you want renamed.

## How it works

1. Uses `scripts/extract_front.py` to pull title, authors, and year from the first pages of the PDF via pdfminer (doesn't require poppler/pdftotext)
2. Formats the name according to the rules above
3. Renames the file with `mv`

Works with:
- Journal articles
- Working papers & preprints
- Government reports
- Books and book chapters
- Any academic/research PDF

Does **not** apply to:
- Periodic series (monthly reports, etc.) — ask for a custom format
- Non-academic documents — other naming rules may apply

## Requirements

- Python 3 with pdfminer.six installed
- Claude Code skill runner
