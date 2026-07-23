"""Record repository.

Joins the extracts from the primary, secondary and archive sources into the
common record model. In this demo build the data is read from a local seed
file; in production the DSNs from the environment are used instead.
"""

from __future__ import annotations

import csv
from datetime import date
from pathlib import Path

from ..models import Location, Record, Status
from .base import DataSource

SEED_FILE = Path(__file__).resolve().parents[3] / "data" / "records_seed.csv"


class RecordRepository(DataSource):
    name = "record_repository"

    def __init__(self, seed_file: Path | None = None) -> None:
        self._seed_file = seed_file or SEED_FILE

    def fetch_records(self) -> list[Record]:
        records: list[Record] = []
        with open(self._seed_file, newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                records.append(self._to_record(row))
        return records

    @staticmethod
    def _to_record(row: dict) -> Record:
        location = Location(
            site=row["site"],
            region=row["region"],
            zone=row["zone"],
            code=row["code"],
        )
        return Record(
            record_id=row["record_id"],
            name=row["name"],
            category=row["category"],
            created_on=date.fromisoformat(row["created_on"]),
            location=location,
            value=float(row["value"]),
            status=Status(row["status"]),
            tags=tuple(t for t in row["tags"].split("|") if t),
        )
