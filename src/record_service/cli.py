"""Command line entry point for the record service."""

from __future__ import annotations

import click

from .config import Settings
from .data_sources import RecordRepository
from .scheduling import ScheduleRunner
from .views import REGISTRY


@click.group()
def cli() -> None:
    """Generate record views."""


@cli.command()
@click.option("--view", "view_slug", required=True, type=click.Choice(sorted(REGISTRY)))
@click.option("--format", "output_format", default="csv", type=click.Choice(["csv", "xlsx"]))
def generate(view_slug: str, output_format: str) -> None:
    """Generate a single view on demand."""
    settings = Settings.load()
    records = RecordRepository().fetch_records()
    view = REGISTRY[view_slug]()
    out_path = view.generate(records, settings.output_dir)
    click.echo(f"Generated {view.title}: {out_path}")


@cli.command("run-scheduled")
def run_scheduled() -> None:
    """Run all views marked as scheduled in the configuration."""
    settings = Settings.load()
    runner = ScheduleRunner(settings.output_dir)
    jobs = runner.jobs_from_config(settings.views)
    outputs = runner.run(jobs)
    click.echo(f"Generated {len(outputs)} scheduled view(s).")
    for path in outputs:
        click.echo(f"  - {path}")


if __name__ == "__main__":
    cli()
