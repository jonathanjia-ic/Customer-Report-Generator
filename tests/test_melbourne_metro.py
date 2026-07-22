"""Tests for the Melbourne Metro Report."""

from report_generator.data_sources import CustomerRepository
from report_generator.reports import MelbourneMetroReport


def _customers():
    return CustomerRepository().fetch_customers()


def test_only_includes_melbourne_metro_suburbs():
    report = MelbourneMetroReport()
    selected = report.select_customers(_customers())

    suburbs = {c.suburb for c in selected}
    assert "Sydney" not in suburbs
    assert "Parramatta" not in suburbs
    assert "Carlton" in suburbs


def test_report_columns():
    report = MelbourneMetroReport()
    assert report.columns[0] == "customer_id"
    assert "residency_status" in report.columns


def test_rows_are_serialisable():
    report = MelbourneMetroReport()
    selected = report.select_customers(_customers())
    for customer in selected:
        row = report.row(customer)
        assert set(row) == set(report.columns)
