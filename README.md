# Record Service

Internal service for generating record views from multiple upstream data
sources. Views are produced on demand or on a regular schedule and are intended
for **internal use only**.

## What it does

- Ingests records from several source systems (primary, secondary, archive).
- Normalises and joins that data into a common record model.
- Renders a catalogue of views (by region, site and tag) to CSV and XLSX.
- Runs views ad hoc via the CLI or automatically via the scheduler.

## View catalogue

| View        | Cadence   | Scope                     |
|-------------|-----------|---------------------------|
| Region View | Weekly    | Records in a given region |
| Site View   | Weekly    | Records at selected sites  |
| Tagged View | Monthly   | Records with a given tag  |

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Generate a single view
python -m record_service.cli generate --view region-north --format xlsx

# Run all scheduled views due now
python -m record_service.cli run-scheduled
```

Configuration lives in [config/settings.yaml](config/settings.yaml). Source
system credentials are read from the environment (see `.env.example`).

## Project layout

```
src/record_service/
  data_sources/   connectors to upstream systems
  models/         common record data model
  views/          one module per view
  scheduling/     schedule definitions and runner
  cli.py          command line entry point
config/           runtime configuration
tests/            unit tests
```

## Support

Raise a ticket or open an issue on this repository.
