"""Tests for the record repository loader."""

from record_service.data_sources import RecordRepository
from record_service.models import Status


def test_loads_all_seed_records():
    records = RecordRepository().fetch_records()
    assert len(records) == 12


def test_status_parsed():
    records = {r.record_id: r for r in RecordRepository().fetch_records()}
    assert records["R0001"].status is Status.ACTIVE
    assert records["R0002"].status is Status.PENDING
    assert records["R0004"].status is Status.INACTIVE


def test_tags_split():
    records = {r.record_id: r for r in RecordRepository().fetch_records()}
    assert "priority" in records["R0002"].tags
