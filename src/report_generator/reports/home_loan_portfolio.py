"""Home Loan Portfolio Report.

Monthly report for the Mortgages Product Team covering customers holding a home
loan product, regardless of location.
"""

from __future__ import annotations

from ..models import Customer
from .base import Report


class HomeLoanPortfolioReport(Report):
    slug = "home-loan-portfolio"
    title = "Home Loan Portfolio"
    columns = (
        "customer_id",
        "full_name",
        "state",
        "segment",
        "total_balance",
    )

    def select_customers(self, customers: list[Customer]) -> list[Customer]:
        return [c for c in customers if "home_loan" in c.products]

    def row(self, customer: Customer) -> dict:
        return {
            "customer_id": customer.customer_id,
            "full_name": customer.full_name,
            "state": customer.residential_address.state,
            "segment": customer.segment,
            "total_balance": f"{customer.total_balance:.2f}",
        }
