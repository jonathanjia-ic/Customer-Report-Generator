"""Common record data model.

This is the normalised shape that every data source is mapped into before
views are rendered. Fields are intentionally source-agnostic.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from enum import Enum


class Status(str, Enum):
    """Lifecycle status of a record, resolved from the primary source."""

    ACTIVE = "active"
    PENDING = "pending"
    INACTIVE = "inactive"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class Location:
    site: str           # specific site / locality
    region: str         # grouping hub, e.g. "north", "central"
    zone: str           # coarse grouping, e.g. "Z1"
    code: str           # short location code
    country: str = "XX"


@dataclass
class Record:
    record_id: str
    name: str
    category: str                      # e.g. "alpha", "beta", "gamma"
    created_on: date
    location: Location
    value: float
    status: Status = Status.UNKNOWN
    tags: tuple[str, ...] = ()

    @property
    def label(self) -> str:
        return f"{self.category}/{self.name}"

    @property
    def site(self) -> str:
        return self.location.site

    @property
    def region(self) -> str:
        return self.location.region
