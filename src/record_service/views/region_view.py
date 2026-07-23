"""Region View.

Covers records assigned to the northern region grouping. Used as an example of
a location-scoped view.
"""

from __future__ import annotations

from ..models import Record
from .base import View


class RegionView(View):
    slug = "region-north"
    title = "Region View"
    columns = (
        "record_id",
        "name",
        "site",
        "code",
        "category",
        "value",
    )

    def select_records(self, records: list[Record]) -> list[Record]:
        return [r for r in records if r.location.region == "north"]

    def row(self, record: Record) -> dict:
        return {
            "record_id": record.record_id,
            "name": record.name,
            "site": record.site,
            "code": record.location.code,
            "category": record.category,
            "value": f"{record.value:.2f}",
        }
