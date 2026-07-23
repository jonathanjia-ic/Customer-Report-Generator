"""Base view class."""

from __future__ import annotations

import abc
import csv
from pathlib import Path

from ..models import Record


class View(abc.ABC):
    """Base class for all views.

    A view selects a subset of records, chooses which columns to show, and
    writes the result to disk. Subclasses implement :meth:`select_records`
    and :meth:`row` and set :attr:`slug`, :attr:`title` and :attr:`columns`.
    """

    slug: str = "view"
    title: str = "View"
    columns: tuple[str, ...] = ()

    def select_records(self, records: list[Record]) -> list[Record]:
        """Return the records that belong in this view. Default: all."""
        return list(records)

    @abc.abstractmethod
    def row(self, record: Record) -> dict:
        """Render a single record as an output row."""
        raise NotImplementedError

    def generate(self, records: list[Record], output_dir: Path) -> Path:
        selected = self.select_records(records)
        output_dir.mkdir(parents=True, exist_ok=True)
        out_path = output_dir / f"{self.slug}.csv"
        with open(out_path, "w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=self.columns)
            writer.writeheader()
            for record in selected:
                writer.writerow(self.row(record))
        return out_path
