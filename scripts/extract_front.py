#!/usr/bin/env python3
"""Print PDF metadata and the text of the first pages, for identifying title/authors/year."""
import sys

from pdfminer.high_level import extract_text
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser


def decode(v):
    if isinstance(v, bytes):
        for enc in ("utf-16", "utf-8", "latin-1"):
            try:
                return v.decode(enc)
            except UnicodeDecodeError:
                continue
    return str(v)


def main(path, pages=3, max_chars=4000):
    with open(path, "rb") as f:
        doc = PDFDocument(PDFParser(f))
        for info in doc.info:
            for key in ("Title", "Author", "Subject", "CreationDate"):
                if key in info:
                    print(f"[meta] {key}: {decode(info[key])}")

    text = extract_text(path, page_numbers=list(range(pages)))
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    out = "\n".join(lines)
    print("----- front text -----")
    print(out[:max_chars] if out else "(no text layer — likely a scanned PDF)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: extract_front.py <file.pdf> [pages]")
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 3)
