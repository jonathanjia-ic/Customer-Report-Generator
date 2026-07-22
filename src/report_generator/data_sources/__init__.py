"""Connectors to upstream source systems.

Each loader returns a list of normalised :class:`~report_generator.models.Customer`
instances so reports never depend on the shape of a particular source system.
"""

from .base import DataSource
from .customer_repository import CustomerRepository

__all__ = ["DataSource", "CustomerRepository"]
