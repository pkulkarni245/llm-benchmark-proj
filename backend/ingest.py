import io

from pypdf import PdfReader
from docx import Document as DocxDocument


def extract_text(filename: str, raw: bytes) -> str:
    lower = filename.lower()
    if lower.endswith(".pdf"):
        reader = PdfReader(io.BytesIO(raw))
        return "\n\n".join(page.extract_text() or "" for page in reader.pages)
    if lower.endswith(".docx"):
        doc = DocxDocument(io.BytesIO(raw))
        return "\n\n".join(p.text for p in doc.paragraphs)
    # txt, md, or anything else: treat as plain text
    return raw.decode("utf-8", errors="ignore")
