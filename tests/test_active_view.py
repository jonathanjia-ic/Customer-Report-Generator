"""Tests for the Active View."""

from record_service.data_sources import RecordRepository
from record_service.models import Status
from record_service.views import ActiveView


def _records():
    return RecordRepository().fetch_records()


def test_only_includes_active_records():
    view = ActiveView()
    selected = view.select_records(_records())

    statuses = {r.status for r in selected}
    assert statuses == {Status.ACTIVE}


def test_view_columns():
    view = ActiveView()
    assert view.columns[0] == "record_id"
    assert "value" in view.columns


def test_rows_are_serialisable():
    view = ActiveView()
    selected = view.select_records(_records())
    for record in selected:
        row = view.row(record)
        assert set(row) == set(view.columns)
