from pathlib import Path


def validate_fastq(path):
    """Check the basic structure of a FASTQ file."""

    lines = Path(path).read_text().splitlines()

    if len(lines) % 4 != 0:
        return False, "File does not contain complete FASTQ records."

    for i in range(0, len(lines), 4):
        header = lines[i]
        sequence = lines[i + 1]
        separator = lines[i + 2]
        quality = lines[i + 3]

        if not header.startswith("@"):
            return False, f"Record {i // 4 + 1}: header does not start with @."

        if not separator.startswith("+"):
            return False, f"Record {i // 4 + 1}: separator does not start with +."

        if len(sequence) != len(quality):
            return False, (
                f"Record {i // 4 + 1}: sequence and quality lengths differ."
            )

    return True, "FASTQ structure is valid."


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Validate the basic structure of a FASTQ file."
    )

    parser.add_argument(
        "fastq",
        help="Path to the FASTQ file to validate.",
    )

    args = parser.parse_args()

    valid, message = validate_fastq(args.fastq)

    if valid:
        print(f"PASS: {message}")
    else:
        print(f"FAIL: {message}")