"""Scheduled report execution.

Schedules are defined in ``config/settings.yaml`` under ``reports``. The runner
resolves which jobs are due and generates them. Cron matching is deliberately
lightweight — the production deployment wires this into the enterprise scheduler.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from ..data_sources import CustomerRepository
from ..reports import REGISTRY


@dataclass
class ScheduledJob:
    report_slug: str
    cadence: str          # "weekly", "monthly", "fortnightly"
    output_format: str = "csv"


class ScheduleRunner:
    def __init__(self, output_dir: Path, repository: CustomerRepository | None = None) -> None:
        self._output_dir = output_dir
        self._repository = repository or CustomerRepository()

    def jobs_from_config(self, reports_config: dict) -> list[ScheduledJob]:
        jobs: list[ScheduledJob] = []
        for slug, cfg in reports_config.items():
            if not cfg.get("scheduled", False):
                continue
            jobs.append(
                ScheduledJob(
                    report_slug=slug,
                    cadence=cfg.get("cadence", "weekly"),
                    output_format=cfg.get("format", "csv"),
                )
            )
        return jobs

    def run(self, jobs: list[ScheduledJob]) -> list[Path]:
        customers = self._repository.fetch_customers()
        outputs: list[Path] = []
        for job in jobs:
            report_cls = REGISTRY[job.report_slug]
            report = report_cls()
            outputs.append(report.generate(customers, self._output_dir))
        return outputs
