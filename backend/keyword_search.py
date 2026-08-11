import math
import re
from collections import Counter

_TOKEN_RE = re.compile(r"\w+")


def _tokenize(text: str) -> list[str]:
    return _TOKEN_RE.findall(text.lower())


class BM25:
    """Minimal BM25 (Okapi) keyword scorer over a fixed corpus."""

    def __init__(self, corpus: list[str], k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self.doc_tokens = [_tokenize(doc) for doc in corpus]
        self.doc_lens = [len(toks) for toks in self.doc_tokens]
        self.n_docs = len(corpus)
        self.avg_doc_len = sum(self.doc_lens) / self.n_docs if self.n_docs else 0.0
        self.doc_freqs = [Counter(toks) for toks in self.doc_tokens]

        term_doc_count: Counter = Counter()
        for toks in self.doc_tokens:
            term_doc_count.update(set(toks))
        self.idf = {
            term: math.log((self.n_docs - df + 0.5) / (df + 0.5) + 1)
            for term, df in term_doc_count.items()
        }

    def scores(self, query: str) -> list[float]:
        query_tokens = _tokenize(query)
        results = []
        for i in range(self.n_docs):
            freqs = self.doc_freqs[i]
            doc_len = self.doc_lens[i]
            score = 0.0
            for term in query_tokens:
                f = freqs.get(term)
                if not f:
                    continue
                idf = self.idf.get(term, 0.0)
                norm = f + self.k1 * (1 - self.b + self.b * doc_len / self.avg_doc_len) if self.avg_doc_len else f
                score += idf * f * (self.k1 + 1) / norm
            results.append(score)
        return results
