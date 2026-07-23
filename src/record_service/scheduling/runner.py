"""Scheduled view execution.

Schedules are defined in ``config/settings.yaml`` under ``views``. The runner
resolves which jobs are due and generates them. Cron matching is deliberately
lightweight — the production deployment wires this into the platform scheduler.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from ..data_sources import RecordRepository
from ..views import REGISTRY


@dataclass
class ScheduledJob:
    view_slug: str
    cadence: str          # "daily", "weekly", "monthly"
    output_format: str = "csv"


class ScheduleRunner:
    def __init__(self, output_dir: Path, repository: RecordRepository | None = None) -> None:
        self._output_dir = output_dir
        self._repository = repository or RecordRepository()

    def jobs_from_config(self, views_config: dict) -> list[ScheduledJob]:
        jobs: list[ScheduledJob] = []
        for slug, cfg in views_config.items():
            if not cfg.get("scheduled", False):
                continue
            jobs.append(
                ScheduledJob(
                    view_slug=slug,
                    cadence=cfg.get("cadence", "weekly"),
                    output_format=cfg.get("format", "csv"),
                )
            )
        return jobs

    def run(self, jobs: list[ScheduledJob]) -> list[Path]:
        records = self._repository.fetch_records()
        outputs: list[Path] = []
        for job in jobs:
            view_cls = REGISTRY[job.view_slug]
            view = view_cls()
            outputs.append(view.generate(records, self._output_dir))
        return outputs
