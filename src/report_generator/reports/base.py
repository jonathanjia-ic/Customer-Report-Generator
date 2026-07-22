"""Base report class."""

from __future__ import annotations

import abc
import csv
from pathlib import Path

from ..models import Customer


class Report(abc.ABC):
    """Base class for all reports.

    A report selects a subset of customers, chooses which columns to show, and
    writes the result to disk. Subclasses implement :meth:`select_customers`
    and :meth:`row` and set :attr:`slug`, :attr:`title` and :attr:`columns`.
    """

    slug: str = "report"
    title: str = "Report"
    columns: tuple[str, ...] = ()

    def select_customers(self, customers: list[Customer]) -> list[Customer]:
        """Return the customers that belong in this report. Default: all."""
        return list(customers)

    @abc.abstractmethod
    def row(self, customer: Customer) -> dict:
        """Render a single customer as an output row."""
        raise NotImplementedError

    def generate(self, customers: list[Customer], output_dir: Path) -> Path:
        selected = self.select_customers(customers)
        output_dir.mkdir(parents=True, exist_ok=True)
        out_path = output_dir / f"{self.slug}.csv"
        with open(out_path, "w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=self.columns)
            writer.writeheader()
            for customer in selected:
                writer.writerow(self.row(customer))
        return out_path
