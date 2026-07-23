"""Tagged View.

Covers records carrying the ``priority`` tag, regardless of location.
"""

from __future__ import annotations

from ..models import Record
from .base import View


class TaggedView(View):
    slug = "tagged"
    title = "Tagged View"
    columns = (
        "record_id",
        "name",
        "zone",
        "category",
        "value",
    )

    def select_records(self, records: list[Record]) -> list[Record]:
        return [r for r in records if "priority" in r.tags]

    def row(self, record: Record) -> dict:
        return {
            "record_id": record.record_id,
            "name": record.name,
            "zone": record.location.zone,
            "category": record.category,
            "value": f"{record.value:.2f}",
        }
