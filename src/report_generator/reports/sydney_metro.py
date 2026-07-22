"""Sydney Metro Report.

Weekly report for NSW Retail Regional Managers covering customers located in the
greater Sydney metropolitan area.
"""

from __future__ import annotations

from ..models import Customer
from .base import Report

SYDNEY_METRO_SUBURBS = frozenset(
    {
        "Sydney",
        "Parramatta",
        "Chatswood",
        "Bondi",
        "Newtown",
        "Manly",
        "Surry Hills",
        "North Sydney",
        "Redfern",
        "Ryde",
    }
)


class SydneyMetroReport(Report):
    slug = "sydney-metro"
    title = "Sydney Metro Report"
    columns = (
        "customer_id",
        "full_name",
        "suburb",
        "postcode",
        "segment",
        "total_balance",
    )

    def select_customers(self, customers: list[Customer]) -> list[Customer]:
        return [c for c in customers if c.suburb in SYDNEY_METRO_SUBURBS]

    def row(self, customer: Customer) -> dict:
        return {
            "customer_id": customer.customer_id,
            "full_name": customer.full_name,
            "suburb": customer.suburb,
            "postcode": customer.residential_address.postcode,
            "segment": customer.segment,
            "total_balance": f"{customer.total_balance:.2f}",
        }
