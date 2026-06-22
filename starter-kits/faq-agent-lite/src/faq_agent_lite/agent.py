from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path


TOKEN_RE = re.compile(r"[a-z0-9]+")
STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "can",
    "do",
    "for",
    "how",
    "i",
    "in",
    "is",
    "my",
    "of",
    "the",
    "to",
    "what",
}

DEFAULT_DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "sample_faqs.csv"

SYNONYMS = {
    "bill": {"billing", "payment", "invoice", "charge"},
    "billing": {"bill", "payment", "invoice", "charge"},
    "cancel": {"cancellation", "stop", "terminate"},
    "change": {"update", "modify", "switch"},
    "claim": {"reimbursement", "request"},
    "document": {"documents", "paperwork", "form", "forms"},
    "password": {"login", "signin", "sign"},
    "refund": {"return", "repay"},
    "move": {"change", "billing", "date"},
    "day": {"date"},
    "paperwork": {"document", "documents", "form", "claim"},
    "required": {"needed", "documents"},
    "signin": {"login", "password"},
    "sign": {"login", "password"},
    "free": {"cooling"},
    "look": {"cooling"},
    "status": {"progress", "state"},
}


@dataclass(frozen=True)
class FAQRecord:
    doc_id: str
    category: str
    question: str
    answer: str
    handoff_note: str


@dataclass(frozen=True)
class AgentAnswer:
    question: str
    answer: str
    source_id: str
    category: str
    confidence: float
    handoff_note: str


def tokenize(text: str) -> set[str]:
    tokens = {token for token in TOKEN_RE.findall(text.lower()) if token not in STOPWORDS}
    expanded = set(tokens)
    for token in tokens:
        expanded.update(SYNONYMS.get(token, set()))
    return expanded


def load_faqs(path: Path | str = DEFAULT_DATA_PATH) -> list[FAQRecord]:
    faq_path = Path(path)
    with faq_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        records = [
            FAQRecord(
                doc_id=row["doc_id"].strip(),
                category=row["category"].strip(),
                question=row["question"].strip(),
                answer=row["answer"].strip(),
                handoff_note=row["handoff_note"].strip(),
            )
            for row in reader
        ]
    if not records:
        raise ValueError(f"No FAQ records found in {faq_path}")
    return records


class FAQAgent:
    def __init__(self, records: list[FAQRecord] | None = None) -> None:
        self.records = records or load_faqs()

    def answer(self, question: str) -> AgentAnswer:
        query_tokens = tokenize(question)
        scored = []
        for record in self.records:
            record_tokens = tokenize(f"{record.category} {record.question} {record.answer}")
            overlap = query_tokens & record_tokens
            score = len(overlap) / max(len(query_tokens), 1)
            scored.append((score, len(overlap), record))

        score, overlap_count, best = max(scored, key=lambda item: (item[0], item[1], item[2].doc_id))
        if overlap_count < 2:
            return AgentAnswer(
                question=question,
                answer=(
                    "I could not find a confident answer in the synthetic FAQ set. "
                    "Please route this to the owner listed in the handoff package."
                ),
                source_id="NO_MATCH",
                category="fallback",
                confidence=0.0,
                handoff_note="Fallback path: add a reviewed FAQ row or route to a human owner.",
            )

        return AgentAnswer(
            question=question,
            answer=best.answer,
            source_id=best.doc_id,
            category=best.category,
            confidence=round(min(score, 1.0), 2),
            handoff_note=best.handoff_note,
        )
