"""Minimal recursive text splitter so students can see exactly how
chunk_size/chunk_overlap affect retrieval, without a library hiding it."""

SEPARATORS = ["\n\n", "\n", ". ", " ", ""]


def split_text(text: str, chunk_size: int, chunk_overlap: int) -> list[str]:
    if chunk_overlap >= chunk_size:
        chunk_overlap = chunk_size // 4
    chunks = _split(text, chunk_size, SEPARATORS)
    return _merge_with_overlap(chunks, chunk_size, chunk_overlap)


def _split(text: str, chunk_size: int, separators: list[str]) -> list[str]:
    if len(text) <= chunk_size:
        return [text] if text.strip() else []

    sep, rest = separators[0], separators[1:]
    if sep == "":
        return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]

    parts = text.split(sep)
    if len(parts) == 1:
        return _split(text, chunk_size, rest)

    pieces: list[str] = []
    for part in parts:
        if len(part) > chunk_size:
            pieces.extend(_split(part, chunk_size, rest))
        elif part.strip():
            pieces.append(part)
    return pieces


def _merge_with_overlap(pieces: list[str], chunk_size: int, chunk_overlap: int) -> list[str]:
    chunks: list[str] = []
    current = ""
    for piece in pieces:
        candidate = f"{current} {piece}".strip() if current else piece
        if len(candidate) <= chunk_size:
            current = candidate
            continue
        if current:
            chunks.append(current)
            current = (current[-chunk_overlap:] + " " + piece).strip() if chunk_overlap else piece
        else:
            current = piece
    if current:
        chunks.append(current)
    return chunks
