"""Report catalogue.

Each report subclasses :class:`~report_generator.reports.base.Report` and is
registered in :data:`REGISTRY` under its CLI slug.
"""

from .base import Report
from .home_loan_portfolio import HomeLoanPortfolioReport
from .melbourne_metro import MelbourneMetroReport
from .sydney_metro import SydneyMetroReport

REGISTRY: dict[str, type[Report]] = {
    "melbourne-metro": MelbourneMetroReport,
    "sydney-metro": SydneyMetroReport,
    "home-loan-portfolio": HomeLoanPortfolioReport,
}

__all__ = [
    "Report",
    "REGISTRY",
    "MelbourneMetroReport",
    "SydneyMetroReport",
    "HomeLoanPortfolioReport",
]
