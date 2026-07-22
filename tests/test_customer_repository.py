"""Tests for the customer repository loader."""

from report_generator.data_sources import CustomerRepository
from report_generator.models import ResidencyStatus


def test_loads_all_seed_customers():
    customers = CustomerRepository().fetch_customers()
    assert len(customers) == 12


def test_residency_status_parsed():
    customers = {c.customer_id: c for c in CustomerRepository().fetch_customers()}
    assert customers["C0001"].residency_status is ResidencyStatus.PERMANENT
    assert customers["C0002"].residency_status is ResidencyStatus.TEMPORARY
    assert customers["C0004"].residency_status is ResidencyStatus.NON_RESIDENT


def test_products_split():
    customers = {c.customer_id: c for c in CustomerRepository().fetch_customers()}
    assert "home_loan" in customers["C0002"].products
