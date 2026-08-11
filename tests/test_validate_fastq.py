from scripts.validate_fastq import validate_fastq


def test_valid_fastq():
    valid, message = validate_fastq("example_data/valid.fastq")

    assert valid is True
    assert message == "FASTQ structure is valid."

def test_invalid_quality():
    valid, message = validate_fastq(
        "example_data/invalid_quality.fastq"
    )

    assert valid is False
    assert "sequence and quality lengths differ" in message

def test_invalid_header():
    valid, message = validate_fastq(
        "example_data/invalid_header.fastq"
    )

    assert valid is False
    assert "header does not start with @" in message

def test_invalid_separator():
    valid, message = validate_fastq(
        "example_data/invalid_separator.fastq"
    )

    assert valid is False
    assert "complete FASTQ records" in message

def test_truncated():
    valid, message = validate_fastq(
        "example_data/truncated.fastq"
    )

    assert valid is False
    assert "complete FASTQ records" in message

def test_empty_sequence():
    valid, message = validate_fastq(
        "example_data/empty_sequence.fastq"
    )

    assert valid is False
    assert "sequence is empty" in message

def test_multiple_reads():
    valid, message = validate_fastq(
        "example_data/multiple_reads.fastq"
    )

    assert valid is True
    assert message == "FASTQ structure is valid."

