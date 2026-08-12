# Bioinformatics File Validation

A Python-based validation tool for checking the basic structural integrity of FASTQ files, with automated regression testing and support for compressed `.fastq.gz` input.

## Project Overview

FASTQ is a common file format used to store sequencing reads and their associated quality scores. Before downstream bioinformatics analysis, it is useful to identify basic structural problems in sequencing files so that malformed input can be detected early.

This project implements a lightweight FASTQ validator that checks structural properties including:

- FASTQ records contain four lines;
- record headers begin with `@`;
- separator lines begin with `+`;
- sequence lines are not empty;
- sequence and quality strings have matching lengths;
- multiple FASTQ records can be processed;
- compressed `.fastq.gz` files can be validated;
- command-line execution returns appropriate exit codes;
- the validator can be installed as a command-line tool.

The project also includes synthetic test data, manual test documentation, and an automated `pytest` regression suite.

## Project Structure

```text
bioinformatics-file-validation/
├── docs/
│   ├── test_cases.md
│   └── validation_plan.md
├── example_data/
│   ├── valid.fastq
│   ├── valid.fastq.gz
│   ├── invalid_header.fastq
│   ├── invalid_quality.fastq
│   ├── invalid_separator.fastq
│   ├── truncated.fastq
│   ├── empty_sequence.fastq
│   ├── empty.fastq
│   ├── empty.fastq.gz
│   ├── multiple_reads.fastq
│   ├── multiple_reads_invalid.fastq
│   ├── multiple_reads_invalid.fastq.gz
│   └── multiple_reads_invalid_header.fastq
├── scripts/
│   ├── __init__.py
│   └── validate_fastq.py
├── tests/
│   └── test_validate_fastq.py
├── .gitignore
├── pyproject.toml
└── README.md
```

All example sequencing files are synthetic test data created specifically for this project and do not contain patient-derived or personally identifiable sequencing data.

## Requirements

The project requires Python 3.11 or later.

`pytest` is used for automated testing. The project is packaged using `pyproject.toml` and setuptools.

The validator itself uses only Python standard-library modules, including:

- `pathlib`
- `gzip`
- `argparse`
- `sys`

## Installation

From the project root, install the project in editable mode:

```bash
python -m pip install -e .
```

This installs the project into the current Python environment and makes the `validate-fastq` command available.

Editable installation is useful during development because changes to the source code can be tested without repeatedly rebuilding and reinstalling the project.

## Running the Validator

### Using the installed command

After installation, the validator can be run using:

```bash
validate-fastq example_data/valid.fastq
```

A valid file produces:

```text
PASS: FASTQ structure is valid.
```

An invalid file produces a `FAIL` message and returns exit code `1`.

For example:

```bash
validate-fastq example_data/invalid_quality.fastq
```

produces:

```text
FAIL: Record 1: sequence and quality lengths differ.
```

The installed command can also process compressed FASTQ files:

```bash
validate-fastq example_data/valid.fastq.gz
```

which produces:

```text
PASS: FASTQ structure is valid.
```

### Running the Python script directly

The Python script can also be executed directly:

```bash
python scripts/validate_fastq.py example_data/valid.fastq
```

A valid file produces:

```text
PASS: FASTQ structure is valid.
```

### Validate a compressed FASTQ file

Compressed input is detected automatically from the `.gz` extension:

```bash
python scripts/validate_fastq.py example_data/valid.fastq.gz
```

### Validate an invalid file

For example:

```bash
python scripts/validate_fastq.py example_data/invalid_quality.fastq
```

The validator reports the structural problem:

```text
FAIL: Record 1: sequence and quality lengths differ.
```

Other malformed inputs can be found in the `example_data/` directory.

## Exit Codes

The command-line validator returns machine-readable exit statuses:

| Exit code | Meaning                 |
| --------: | ----------------------- |
|       `0` | FASTQ passed validation |
|       `1` | FASTQ failed validation |

For example:

```bash
validate-fastq example_data/valid.fastq
echo $?
```

returns:

```text
0
```

An invalid file returns:

```text
1
```

This allows the validator to be incorporated into shell scripts or larger automated workflows.

## Automated Testing

The project uses `pytest` for automated regression testing.

Run the complete test suite with:

```bash
python -m pytest
```

The current test suite contains **13 automated tests** covering:

- valid FASTQ input;
- sequence/quality length mismatches;
- malformed headers;
- malformed separator lines;
- truncated records;
- empty sequences;
- multiple valid records;
- valid compressed FASTQ input;
- empty FASTQ files;
- empty compressed FASTQ files;
- invalid later records;
- invalid compressed FASTQ input;
- malformed headers occurring in later records.

The current test suite passes:

```text
13 passed
```

The tests are designed to verify both successful validation and correct rejection of deliberately malformed input.

## Test Data

The `example_data/` directory contains small synthetic FASTQ examples representing both valid and invalid scenarios.

Examples include:

- valid single-record FASTQ;
- valid multiple-record FASTQ;
- invalid headers;
- invalid separator lines;
- sequence/quality length mismatches;
- empty sequences;
- truncated records;
- empty FASTQ files;
- invalid records occurring later in a file;
- compressed FASTQ input.

This provides reproducible input for both manual and automated validation.

## Documentation

Detailed manual test cases are documented in:

```text
docs/test_cases.md
```

The validation approach and project acceptance criteria are documented in:

```text
docs/validation_plan.md
```

The test-case documentation distinguishes between:

- **Expected Result** — the behaviour defined before testing;
- **Observed Result** — the behaviour produced by the validator;
- **Test Result** — whether the observed behaviour matched the expected behaviour.

This distinction is important because an invalid FASTQ file is expected to produce a `FAIL` message from the validator, while the corresponding software test should still be recorded as `PASS` when the validator correctly identifies the invalid input.

## Current Scope

The validator currently focuses on **basic FASTQ structural validation**.

It does not attempt to provide full biological or sequence-quality validation. For example, the current implementation does not validate:

- nucleotide alphabet restrictions;
- FASTQ quality-score encoding ranges;
- biological sequence content;
- read identifiers against a specific naming convention;
- paired-end relationships between separate FASTQ files;
- sequencing-platform-specific requirements.

These are outside the current scope and could be considered in future development.

## Future Improvements

Potential future improvements include:

1. more specific diagnostics for individual FASTQ formatting problems;
2. reporting affected record and line numbers where appropriate;
3. reporting multiple validation errors instead of stopping at the first failure;
4. additional FASTQ edge cases and regression tests;
5. configurable command-line output or validation modes;
6. extension to additional bioinformatics file formats.

## Project Goals

This project is intended to demonstrate practical software development and testing skills in a bioinformatics context, including:

- Python programming;
- command-line tool development;
- Python package configuration;
- installed command-line interfaces;
- FASTQ file handling;
- compressed-file processing;
- automated testing with `pytest`;
- negative and edge-case testing;
- regression testing;
- synthetic test-data design;
- meaningful error reporting;
- machine-readable exit codes;
- technical documentation;
- Git version control.

The emphasis is on building a small, reproducible, testable bioinformatics utility rather than implementing a full production-grade FASTQ parser.
