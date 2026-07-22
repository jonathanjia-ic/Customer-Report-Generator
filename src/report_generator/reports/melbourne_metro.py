"""Melbourne Metro Report.

Weekly report for VIC Retail Regional Managers covering customers whose
permanent residential address falls within the Greater Melbourne metropolitan
area. Used to guide branch-level product and staffing decisions.

The Greater Melbourne metropolitan area is defined as residential postcodes in
the range 3000-3207 inclusive. Customers outside that range, or without a valid
residential address on file, are excluded.
"""

from __future__ import annotations

from ..models import Customer
from .base import Report

# Greater Melbourne metropolitan postcode range (inclusive).
MELBOURNE_METRO_POSTCODE_MIN = 3000
MELBOURNE_METRO_POSTCODE_MAX = 3207
MELBOURNE_METRO_POSTCODE_RANGE = (
    f"{MELBOURNE_METRO_POSTCODE_MIN}-{MELBOURNE_METRO_POSTCODE_MAX}"
)

# Suburbs that sit within the Greater Melbourne metropolitan postcode range.
MELBOURNE_METRO_SUBURBS = frozenset(
    {
        "Melbourne",
        "Carlton",
        "Fitzroy",
        "Richmond",
        "South Yarra",
        "St Kilda",
        "Brunswick",
        "Footscray",
        "Prahran",
        "Docklands",
    }
)


def _has_valid_residential_address(customer: Customer) -> bool:
    """True when the customer has a usable residential address on file."""
    address = customer.residential_address
    return bool(address and address.suburb and address.postcode)


class MelbourneMetroReport(Report):
    slug = "melbourne-metro"
    title = f"Melbourne Metro Report (postcodes {MELBOURNE_METRO_POSTCODE_RANGE})"
    columns = (
        "customer_id",
        "full_name",
        "suburb",
        "postcode",
        "segment",
        "total_balance",
    )

    def select_customers(self, customers: list[Customer]) -> list[Customer]:
        return [
            c
            for c in customers
            if _has_valid_residential_address(c)
            and c.suburb in MELBOURNE_METRO_SUBURBS
        ]

    def row(self, customer: Customer) -> dict:
        return {
            "customer_id": customer.customer_id,
            "full_name": customer.full_name,
            "suburb": customer.suburb,
            "postcode": customer.residential_address.postcode,
            "segment": customer.segment,
            "total_balance": f"{customer.total_balance:.2f}",
        }
