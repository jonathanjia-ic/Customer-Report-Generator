"""Common customer data model.

This is the normalised shape that every data source is mapped into before
reports are rendered. Fields are intentionally source-agnostic.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from enum import Enum


class ResidencyStatus(str, Enum):
    """KYC residency classification, sourced from the CRM."""

    PERMANENT = "permanent"
    TEMPORARY = "temporary"
    NON_RESIDENT = "non_resident"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class Address:
    line1: str
    suburb: str
    city: str           # nearest capital city, as provided by the customer
    state: str          # e.g. "VIC", "NSW"
    postcode: str
    country: str = "AU"


@dataclass
class Customer:
    customer_id: str
    first_name: str
    last_name: str
    date_of_birth: date
    email: str
    segment: str                       # e.g. "retail", "premier", "business"
    residential_address: Address
    total_balance: float
    residency_status: ResidencyStatus = ResidencyStatus.UNKNOWN
    products: tuple[str, ...] = ()

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def suburb(self) -> str:
        return self.residential_address.suburb
