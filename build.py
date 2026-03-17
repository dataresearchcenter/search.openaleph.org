#!/usr/bin/env python3
"""Build JSON files from YAML sources."""

import json
import sys
from pathlib import Path

import yaml

SRC_DIR = Path(__file__).parent
OUT_DIR = SRC_DIR / "dist"

FILES = {
    "topics.yml": "topics.json",
    "dataset_groups.yml": "dataset_groups.json",
}


def build():
    OUT_DIR.mkdir(exist_ok=True)
    for src_name, dst_name in FILES.items():
        src = SRC_DIR / src_name
        dst = OUT_DIR / dst_name
        with open(src) as f:
            data = yaml.safe_load(f)
        with open(dst, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"{src_name} -> dist/{dst_name}")


if __name__ == "__main__":
    build()
