"""Active View.

Covers records currently in the active state, regardless of location or tag.
"""

from __future__ import annotations

from ..models import Record, Status
from .base import View


class ActiveView(View):
    slug = "active"
    title = "Active View"
    columns = (
        "record_id",
        "name",
        "region",
        "category",
        "value",
    )

    def select_records(self, records: list[Record]) -> list[Record]:
        return [r for r in records if r.status is Status.ACTIVE]

    def row(self, record: Record) -> dict:
        return {
            "record_id": record.record_id,
            "name": record.name,
            "region": record.region,
            "category": record.category,
            "value": f"{record.value:.2f}",
        }
