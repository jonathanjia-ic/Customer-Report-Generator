"""Command line entry point for Region Based Customer Reporting."""

from __future__ import annotations

import click

from .config import Settings
from .data_sources import CustomerRepository
from .reports import REGISTRY
from .scheduling import ScheduleRunner


@click.group()
def cli() -> None:
    """Generate customer reports."""


@cli.command()
@click.option("--report", "report_slug", required=True, type=click.Choice(sorted(REGISTRY)))
@click.option("--format", "output_format", default="csv", type=click.Choice(["csv", "xlsx"]))
def generate(report_slug: str, output_format: str) -> None:
    """Generate a single report on demand."""
    settings = Settings.load()
    customers = CustomerRepository().fetch_customers()
    report = REGISTRY[report_slug]()
    out_path = report.generate(customers, settings.output_dir)
    click.echo(f"Generated {report.title}: {out_path}")


@cli.command("run-scheduled")
def run_scheduled() -> None:
    """Run all reports marked as scheduled in the configuration."""
    settings = Settings.load()
    runner = ScheduleRunner(settings.output_dir)
    jobs = runner.jobs_from_config(settings.reports)
    outputs = runner.run(jobs)
    click.echo(f"Generated {len(outputs)} scheduled report(s).")
    for path in outputs:
        click.echo(f"  - {path}")


if __name__ == "__main__":
    cli()
