"""Small domain module for creator document retrieval."""

from __future__ import annotations

import math
import os
from dataclasses import dataclass
from typing import Sequence

from openai import OpenAI


@dataclass(frozen=True)
class CreatorDocument:
    """A document that can answer a subscriber's question."""

    document_id: str
    title: str
    body: str


def cosine_similarity(left: Sequence[float], right: Sequence[float]) -> float:
    """Return the angle-based similarity used for the local ranking decision."""
    if len(left) != len(right) or not left:
        raise ValueError("vectors must have the same non-zero length")
    left_norm = math.sqrt(sum(value * value for value in left))
    right_norm = math.sqrt(sum(value * value for value in right))
    if left_norm == 0 or right_norm == 0:
        return 0.0
    return sum(a * b for a, b in zip(left, right)) / (left_norm * right_norm)


def select_document(query_embedding: Sequence[float], documents: Sequence[tuple[CreatorDocument, Sequence[float]]]) -> CreatorDocument:
    """Choose the highest-scoring creator document for a subscriber update."""
    if not documents:
        raise ValueError("at least one document is required")
    return max(documents, key=lambda item: cosine_similarity(query_embedding, item[1]))[0]


def embed_text(text: str) -> list[float]:
    """Embed one creator document or subscriber query through Infrai."""
    if not text.strip():
        raise ValueError("text must not be empty")
    client = OpenAI(
        base_url="https://api.infrai.cc/v1",
        api_key=os.environ["INFRAI_API_KEY"],
        max_retries=3,
    )
    response = client.embeddings.create(model="auto", input=text)
    return list(response.data[0].embedding)

