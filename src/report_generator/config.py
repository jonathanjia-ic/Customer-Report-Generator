"""Runtime configuration loading."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

import yaml

DEFAULT_CONFIG_PATH = Path(__file__).resolve().parents[2] / "config" / "settings.yaml"


@dataclass
class Settings:
    output_dir: Path
    log_level: str
    sources: dict = field(default_factory=dict)
    reports: dict = field(default_factory=dict)

    @classmethod
    def load(cls, path: Path | None = None) -> "Settings":
        path = path or DEFAULT_CONFIG_PATH
        with open(path, "r", encoding="utf-8") as fh:
            raw = yaml.safe_load(fh)

        output_dir = Path(os.getenv("REPORT_OUTPUT_DIR", raw.get("output_dir", "./output")))
        return cls(
            output_dir=output_dir,
            log_level=os.getenv("LOG_LEVEL", raw.get("log_level", "INFO")),
            sources=raw.get("sources", {}),
            reports=raw.get("reports", {}),
        )
