"""Filter identified records for screening."""

import csv
import sys
from pathlib import Path

INPUT_PATH = Path("step-2-prisma/identified.csv")
OUTPUT_PATH = Path("step-2-prisma/screened.csv")
DOCUMENT_TYPES = {
    "Article",
    "Book chapter",
    "Conference paper",
    "Conference review",
    "Review",
}

csv.field_size_limit(sys.maxsize)


def main() -> None:
    with INPUT_PATH.open(encoding="utf-8-sig", newline="") as input_file:
        reader = csv.DictReader(input_file)
        with OUTPUT_PATH.open("w", encoding="utf-8", newline="") as output_file:
            if reader.fieldnames is None:
                raise ValueError("Input CSV is missing a header row")
            writer = csv.DictWriter(
                output_file, fieldnames=[*reader.fieldnames, "seelcted"]
            )
            writer.writeheader()

            for row in reader:
                abstract = row["Abstract"].strip()
                if (
                    row["Document Type"].strip() in DOCUMENT_TYPES
                    and row["Language of Original Document"].strip() == "English"
                    and len(abstract) > 80
                ):
                    row["seelcted"] = False
                    writer.writerow(row)


if __name__ == "__main__":
    main()
