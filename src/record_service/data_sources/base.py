"""Base class for data source connectors."""

from __future__ import annotations

import abc

from ..models import Record


class DataSource(abc.ABC):
    """A connector that yields normalised records."""

    name: str = "unnamed"

    @abc.abstractmethod
    def fetch_records(self) -> list[Record]:
        """Return all records available from this source system."""
        raise NotImplementedError
