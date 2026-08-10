# FASTQ Validation Project — Validation Plan

## 1. Purpose

The purpose of this validation plan is to define the approach used to evaluate the FASTQ structural validation tool developed in this repository.

The project demonstrates a small, reproducible software testing workflow using synthetic sequencing-style data. The validation process is designed to assess whether the validator behaves as expected when presented with both valid and deliberately malformed FASTQ inputs.

The project is intended as a learning and portfolio exercise in bioinformatics software testing. It is not a clinical diagnostic tool and has not been developed or validated for clinical use.

---

## 2. Scope

The validation activities cover structural checks implemented by the Python FASTQ validator.

The current scope includes:

* identification of FASTQ record boundaries;
* validation of FASTQ header structure;
* validation of the `+` separator;
* detection of incomplete or truncated records;
* detection of empty sequence fields;
* comparison of sequence and quality-string lengths;
* processing of multiple FASTQ records;
* command-line execution using the project's `argparse` interface.

Future validation activities will extend this scope to include compressed FASTQ input, additional edge cases, automated regression testing, and command-line exit codes.

---

## 3. Out of Scope

The following activities are outside the scope of this project:

* clinical diagnostic validation;
* validation against patient-derived sequencing data;
* regulatory certification;
* demonstration of compliance with IEC 62304, ISO 13485, ISO 14971 or other medical-device standards;
* biological interpretation of sequencing results;
* assessment of sequencing accuracy or instrument performance;
* full validation of downstream alignment, variant calling, or clinical bioinformatics pipelines.

The project uses synthetic example data rather than patient or personally identifiable sequencing data.

---

## 4. Test Strategy

Testing follows a combination of positive and negative test cases.

### Positive testing

Positive tests use inputs that are expected to satisfy the structural rules implemented by the validator.

Examples include:

* a valid FASTQ record;
* multiple valid FASTQ records.

The expected outcome is successful validation.

### Negative testing

Negative tests deliberately introduce structural problems into FASTQ records.

Examples include:

* malformed headers;
* missing `+` separators;
* truncated records;
* empty sequences;
* sequence and quality length mismatches.

The expected outcome is that the validator rejects the input and reports a failure.

Negative testing is particularly important because the validator is intended to identify malformed input rather than simply process valid examples.

---

## 5. Test Data

The project uses small synthetic FASTQ files created specifically for testing.

The test data is designed to be:

* reproducible;
* small enough to inspect manually;
* free from patient-derived information;
* deliberately constructed to exercise specific validation conditions.

The current example data includes:

| File                      | Purpose                          |
| ------------------------- | -------------------------------- |
| `valid.fastq`             | Valid FASTQ record               |
| `invalid_quality.fastq`   | Sequence/quality length mismatch |
| `invalid_header.fastq`    | Malformed FASTQ header           |
| `invalid_separator.fastq` | Missing `+` separator            |
| `truncated.fastq`         | Incomplete FASTQ record          |
| `empty_sequence.fastq`    | Empty sequence field             |
| `multiple_reads.fastq`    | Multiple valid FASTQ records     |

---

## 6. Expected Behaviour

The validator should:

1. accept correctly structured FASTQ input;
2. reject malformed FASTQ input;
3. identify structural problems where supported by the implementation;
4. provide a clear validation result;
5. process multiple records within the same input file;
6. behave consistently when the same input is tested repeatedly.

Expected behaviour is defined before execution where possible and compared with the observed program output after execution.

---

## 7. Test Execution and Recording

Each test case is assigned a unique test identifier.

The associated test documentation records:

* test ID;
* objective;
* input data;
* expected result;
* observed result;
* overall test result;
* relevant notes or limitations.

The distinction between validator output and software test outcome is maintained throughout the project.

For example, an invalid FASTQ file is expected to produce a validator `FAIL` message. If the validator correctly rejects that invalid input, the corresponding software test has passed.

---

## 8. Acceptance Criteria

The current implementation is considered to meet the project's structural validation objectives when:

* valid FASTQ examples are accepted;
* deliberately malformed FASTQ examples are rejected;
* sequence and quality length mismatches are detected;
* incomplete records are rejected;
* multiple valid records can be processed;
* expected and observed behaviour are documented;
* automated tests reproduce the key manual test cases;
* command-line execution produces an appropriate machine-readable exit status.

Acceptance criteria may be expanded as additional functionality is implemented.

---

## 9. Defect and Improvement Handling

When observed behaviour differs from expected behaviour, the discrepancy will be recorded and investigated before modifying the implementation.

Where appropriate, improvements will be followed by repeat testing to determine whether the change resolves the identified issue without introducing a regression.

Particular attention will be given to the clarity and usefulness of validation error messages.

---

## 10. Traceability

The project will maintain a simple relationship between validation requirements, test cases, test data, and implementation.

The intended relationship is:

```text
Validation requirement
        ↓
Test case
        ↓
Synthetic test input
        ↓
Validator execution
        ↓
Observed result
        ↓
Test result
```

This lightweight traceability approach is intended to demonstrate structured testing practice rather than formal medical-device regulatory compliance.

---

## 11. Automation

Manual tests will be progressively converted into automated tests using `pytest`.

The automated test suite will provide regression coverage for the validator and will allow multiple test cases to be executed consistently after changes to the implementation.

The project will implement command-line exit codes so that validation results can be consumed by other software or shell-based workflows rather than relying solely on printed messages.

---

## 12. Future Validation

Planned extensions include:

* additional FASTQ edge cases;
* improved diagnostic error messages;
* meaningful command-line exit codes;
* automated `pytest` coverage;
* `.fastq.gz` input support;
* demonstrations using `samtools`;
* demonstrations using `bcftools`;
* expanded project documentation.

These features will only be described as completed once they have been implemented and tested in the repository.
