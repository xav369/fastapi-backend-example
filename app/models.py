from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Item:
    id: int
    name: str
    description: str | None = None
