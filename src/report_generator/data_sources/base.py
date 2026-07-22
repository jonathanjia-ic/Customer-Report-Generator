"""Base class for data source connectors."""

from __future__ import annotations

import abc

from ..models import Customer


class DataSource(abc.ABC):
    """A connector that yields normalised customer records."""

    name: str = "unnamed"

    @abc.abstractmethod
    def fetch_customers(self) -> list[Customer]:
        """Return all customers available from this source system."""
        raise NotImplementedError
