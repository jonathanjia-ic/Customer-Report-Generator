"""Customer repository.

Joins the core banking, CRM and marketing data warehouse extracts into the
common customer model. In this demo build the data is read from a local seed
file; in production the DSNs from the environment are used instead.
"""

from __future__ import annotations

import csv
from datetime import date
from pathlib import Path

from ..models import Address, Customer, ResidencyStatus
from .base import DataSource

SEED_FILE = Path(__file__).resolve().parents[3] / "data" / "customers_seed.csv"


class CustomerRepository(DataSource):
    name = "customer_repository"

    def __init__(self, seed_file: Path | None = None) -> None:
        self._seed_file = seed_file or SEED_FILE

    def fetch_customers(self) -> list[Customer]:
        customers: list[Customer] = []
        with open(self._seed_file, newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                customers.append(self._to_customer(row))
        return customers

    @staticmethod
    def _to_customer(row: dict) -> Customer:
        address = Address(
            line1=row["address_line1"],
            suburb=row["suburb"],
            city=row["city"],
            state=row["state"],
            postcode=row["postcode"],
        )
        return Customer(
            customer_id=row["customer_id"],
            first_name=row["first_name"],
            last_name=row["last_name"],
            date_of_birth=date.fromisoformat(row["date_of_birth"]),
            email=row["email"],
            segment=row["segment"],
            residency_status=ResidencyStatus(row["residency_status"]),
            residential_address=address,
            total_balance=float(row["total_balance"]),
            products=tuple(p for p in row["products"].split("|") if p),
        )
