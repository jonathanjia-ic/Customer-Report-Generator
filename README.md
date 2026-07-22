# Customer Report Generator

Internal reporting service for generating customer reports from multiple upstream
data sources. Reports are produced on demand or on a regular schedule and are
intended for **internal use only**. Many consumers are non-technical stakeholders
(branch managers, business analysts, product owners) who use these reports to
guide business decisions.

> ⚠️ **Confidential** — Reports contain customer information subject to the
> Privacy Act 1988 (Cth) and internal data handling policy DP-207. Do not
> distribute outside the organisation.

## What it does

- Ingests customer, account, and transaction data from several source systems
  (core banking, CRM, marketing data warehouse).
- Normalises and joins that data into a common customer model.
- Renders a catalogue of reports (regional, product, risk, retention) to CSV,
  XLSX and PDF.
- Runs reports ad hoc via the CLI or automatically via the scheduler.

## Report catalogue

| Report                 | Cadence   | Audience                     |
|------------------------|-----------|------------------------------|
| Melbourne Metro Report | Weekly    | VIC Retail Regional Managers |
| Sydney Metro Report    | Weekly    | NSW Retail Regional Managers |
| Home Loan Portfolio    | Monthly   | Mortgages Product Team       |
| Customer Retention     | Fortnight | Retention & Marketing        |

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Generate a single report
python -m report_generator.cli generate --report melbourne-metro --format xlsx

# Run all scheduled reports due now
python -m report_generator.cli run-scheduled
```

Configuration lives in [config/settings.yaml](config/settings.yaml). Source
system credentials are read from the environment (see `.env.example`).

## Project layout

```
src/report_generator/
  data_sources/   connectors to upstream systems
  models/         common customer / account data model
  reports/        one module per report
  scheduling/     schedule definitions and runner
  cli.py          command line entry point
config/           runtime configuration
tests/            unit tests
```

## Support

Owned by the **Customer Insights** team. Questions in `#customer-insights` or
raise a ticket against the `CRG` Jira project.
