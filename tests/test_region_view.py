"""Tests for the Region View."""

from record_service.data_sources import RecordRepository
from record_service.views import RegionView


def _records():
    return RecordRepository().fetch_records()


def test_only_includes_northern_region():
    view = RegionView()
    selected = view.select_records(_records())

    regions = {r.location.region for r in selected}
    assert "south" not in regions
    assert "east" not in regions
    assert "north" in regions


def test_view_columns():
    view = RegionView()
    assert view.columns[0] == "record_id"
    assert "category" in view.columns


def test_rows_are_serialisable():
    view = RegionView()
    selected = view.select_records(_records())
    for record in selected:
        row = view.row(record)
        assert set(row) == set(view.columns)
