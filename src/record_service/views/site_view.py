"""Site View.

Covers records located at one of a fixed set of named sites.
"""

from __future__ import annotations

from ..models import Record
from .base import View

SELECTED_SITES = frozenset(
    {
        "Site A",
        "Site B",
        "Site C",
        "Site D",
        "Site E",
        "Site F",
        "Site G",
        "Site H",
        "Site I",
        "Site J",
    }
)


class SiteView(View):
    slug = "site"
    title = "Site View"
    columns = (
        "record_id",
        "name",
        "site",
        "code",
        "category",
        "value",
    )

    def select_records(self, records: list[Record]) -> list[Record]:
        return [r for r in records if r.site in SELECTED_SITES]

    def row(self, record: Record) -> dict:
        return {
            "record_id": record.record_id,
            "name": record.name,
            "site": record.site,
            "code": record.location.code,
            "category": record.category,
            "value": f"{record.value:.2f}",
        }
