"""Connectors to upstream source systems.

Each loader returns a list of normalised :class:`~record_service.models.Record`
instances so views never depend on the shape of a particular source system.
"""

from .base import DataSource
from .record_repository import RecordRepository

__all__ = ["DataSource", "RecordRepository"]
