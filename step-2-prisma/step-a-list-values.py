"""Print the values used for document type and language."""

import csv
import sys
from pathlib import Path


INPUT_PATH = Path("step-2-prisma/identified.csv")

csv.field_size_limit(sys.maxsize)


def main() -> None:
    with INPUT_PATH.open(encoding="utf-8-sig", newline="") as file:
        rows = list(csv.DictReader(file))

    columns = {
        "Document types": "Document Type",
        "Languages": "Language of Original Document",
    }

    for label, column in columns.items():
        values = sorted({row[column].strip() for row in rows if row[column].strip()})
        print(f"{label}:")
        for value in values:
            print(f"- {value}")


if __name__ == "__main__":
    main()
