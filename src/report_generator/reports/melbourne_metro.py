"""Melbourne Metro Report.

Weekly report for VIC Retail Regional Managers covering customers located in the
greater Melbourne metropolitan area. Used to guide branch-level product and
staffing decisions.
"""

from __future__ import annotations

from ..models import Customer
from .base import Report


class MelbourneMetroReport(Report):
    slug = "melbourne-metro"
    title = "Melbourne Metro Report"
    columns = (
        "customer_id",
        "full_name",
        "suburb",
        "postcode",
        "segment",
        "total_balance",
    )

    def select_customers(self, customers: list[Customer]) -> list[Customer]:
        return [c for c in customers if c.residential_address.city == "Melbourne"]

    def row(self, customer: Customer) -> dict:
        return {
            "customer_id": customer.customer_id,
            "full_name": customer.full_name,
            "suburb": customer.suburb,
            "postcode": customer.residential_address.postcode,
            "segment": customer.segment,
            "total_balance": f"{customer.total_balance:.2f}",
        }
