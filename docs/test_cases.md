# FASTQ Validation Test Cases

## 1. Purpose

This document records manual test cases used to evaluate the FASTQ structural validation script in this repository.

The test cases are designed to verify that the validator:

* accepts correctly structured FASTQ records;
* rejects malformed FASTQ records;
* identifies sequence and quality length mismatches;
* handles incomplete records;
* processes multiple FASTQ records;
* provides a clear pass/fail outcome.

The example FASTQ files used for these tests are synthetic test data created specifically for this project. They do not contain patient-derived or personally identifiable sequencing data.

---

## 2. Test Result Terminology

The terms **Expected Result**, **Observed Result**, and **Test Result** are used as follows:

* **Expected Result** — the behaviour defined before executing the test.
* **Observed Result** — the behaviour produced by the validator when the test was executed.
* **Test Result** — whether the observed behaviour matched the expected behaviour.

A `PASS` or `FAIL` reported by the validator refers to the validity of the input FASTQ file. It does not directly indicate whether the software test itself passed.

For example, an invalid FASTQ file is expected to produce a `FAIL` message from the validator. If it does so correctly, the corresponding software test is considered to have **PASSED**.

---

## 3. Manual Test Cases

### TC-001 — Valid FASTQ

**Objective:**
Verify that the validator accepts a correctly structured FASTQ record.

**Input:**
`example_data/valid.fastq`

**Expected Result:**
The validator should accept the FASTQ structure and report `PASS`.

**Observed Result:**
`PASS: FASTQ structure is valid.`

**Test Result:**
PASS

**Notes:**
The test confirms that a correctly structured FASTQ record is accepted.

---

### TC-002 — Sequence/Quality Length Mismatch

**Objective:**
Verify that the validator detects a difference between the sequence length and quality-string length.

**Input:**
`example_data/invalid_quality.fastq`

**Expected Result:**
The validator should reject the record and report that the sequence and quality lengths differ.

**Observed Result:**
`FAIL: Record 1: sequence and quality lengths differ.`

**Test Result:**
PASS

**Notes:**
The validator correctly identified the structural inconsistency.

---

### TC-003 — Malformed FASTQ Header

**Objective:**
Verify that the validator rejects a FASTQ record whose header does not begin with `@`.

**Input:**
`example_data/invalid_header.fastq`

**Expected Result:**
The validator should reject the record because the FASTQ header is malformed.

**Observed Result:**
The validator reported a failure for the malformed record.

**Test Result:**
PASS

**Notes:**
The test demonstrates negative testing using deliberately malformed input.

---

### TC-004 — Missing `+` Separator

**Objective:**
Verify that the validator rejects a FASTQ record missing the required `+` separator line.

**Input:**
`example_data/invalid_separator.fastq`

**Expected Result:**
The validator should reject the incomplete FASTQ record.

**Observed Result:**
`FAIL: File does not contain complete FASTQ records.`

**Test Result:**
PASS

**Notes:**
The validator correctly rejected the three-line record. The current implementation does not yet provide a specific diagnostic identifying the missing `+` separator.

---

### TC-005 — Truncated FASTQ Record

**Objective:**
Verify that the validator rejects a FASTQ record that does not contain all four required lines.

**Input:**
`example_data/truncated.fastq`

**Expected Result:**
The validator should reject the incomplete record.

**Observed Result:**
`FAIL: File does not contain complete FASTQ records.`

**Test Result:**
PASS

**Notes:**
The validator correctly detected that the record was incomplete.

---

### TC-006 — Empty Sequence

**Objective:**
Verify that the validator rejects a FASTQ record containing an empty sequence.

**Input:**
`example_data/empty_sequence.fastq`

**Expected Result:**
The validator should reject the record because the sequence is empty.

**Observed Result:**
`FAIL: Record 1: sequence and quality lengths differ.`

**Test Result:**
PASS

**Notes:**
The validator rejected the invalid record. The current diagnostic identifies the resulting length mismatch rather than explicitly stating that the sequence is empty. This may be improved in a later implementation step.

---

### TC-007 — Multiple FASTQ Records

**Objective:**
Verify that the validator can process more than one FASTQ record in a single input file.

**Input:**
`example_data/multiple_reads.fastq`

**Expected Result:**
The validator should process all records and report `PASS` when all records are structurally valid.

**Observed Result:**
`PASS: FASTQ structure is valid.`

**Test Result:**
PASS

**Notes:**
The test confirms that the validator can process multiple valid records rather than only a single FASTQ record.

---

## 4. Summary of Manual Testing

| Test ID | Scenario                  | Expected | Observed | Test Result |
| ------- | ------------------------- | -------- | -------- | ----------- |
| TC-001  | Valid FASTQ               | PASS     | PASS     | PASS        |
| TC-002  | Sequence/quality mismatch | FAIL     | FAIL     | PASS        |
| TC-003  | Malformed header          | FAIL     | FAIL     | PASS        |
| TC-004  | Missing `+` separator     | FAIL     | FAIL     | PASS        |
| TC-005  | Truncated record          | FAIL     | FAIL     | PASS        |
| TC-006  | Empty sequence            | FAIL     | FAIL     | PASS        |
| TC-007  | Multiple records          | PASS     | PASS     | PASS        |

## 5. Expanded Edge-Case Tests

The validation suite was expanded to cover additional edge cases and compressed FASTQ input.

### TC-008 — Empty FASTQ File

**Objective:**
Verify that the validator rejects an empty FASTQ file.

**Input:**
`example_data/empty.fastq`

**Expected Result:**
The validator should reject the file and report that it contains no records.

**Observed Result:**
`FAIL: FASTQ file contains no records.`

**Test Result:**
PASS

**Notes:**
An empty FASTQ file contains no sequencing records and is therefore rejected.

---

### TC-009 — Empty Compressed FASTQ File

**Objective:**
Verify that the validator rejects an empty compressed FASTQ file.

**Input:**
`example_data/empty.fastq.gz`

**Expected Result:**
The validator should reject the file and report that it contains no records.

**Observed Result:**
`FAIL: FASTQ file contains no records.`

**Test Result:**
PASS

**Notes:**
This confirms that the empty-file validation behaviour is also applied to `.fastq.gz` input.

---

### TC-010 — Invalid Later Record

**Objective:**
Verify that the validator identifies a structural error occurring in a later FASTQ record.

**Input:**
`example_data/multiple_reads_invalid.fastq`

**Expected Result:**
The validator should reject the file and identify the sequence/quality length mismatch in Record 2.

**Observed Result:**
`FAIL: Record 2: sequence and quality lengths differ.`

**Test Result:**
PASS

**Notes:**
Record 1 is valid, while Record 2 contains the deliberate sequence/quality length mismatch. The validator reports the first validation failure encountered.

---

### TC-011 — Invalid Compressed Later Record

**Objective:**
Verify that the validator detects a structural error occurring in a later record of a compressed FASTQ file.

**Input:**
`example_data/multiple_reads_invalid.fastq.gz`

**Expected Result:**
The validator should reject the file and identify the sequence/quality length mismatch in Record 2.

**Observed Result:**
`FAIL: Record 2: sequence and quality lengths differ.`

**Test Result:**
PASS

**Notes:**
This confirms consistent validation behaviour between uncompressed and compressed FASTQ input.

---

### TC-012 — Invalid Header in Later Record

**Objective:**
Verify that the validator detects a malformed header occurring after an earlier valid record.

**Input:**
`example_data/multiple_reads_invalid_header.fastq`

**Expected Result:**
The validator should reject the file and identify the malformed header in Record 2.

**Observed Result:**
`FAIL: Record 2: header does not start with @.`

**Test Result:**
PASS

**Notes:**
Record 1 is valid and Record 2 contains the deliberate malformed header.

---

## 6. Automated Regression Testing

The manual validation cases are supplemented by automated regression tests using `pytest`.

The automated test suite currently contains 13 tests covering:

* valid FASTQ input;
* sequence/quality length mismatches;
* malformed headers;
* missing separators;
* truncated records;
* empty sequences;
* multiple valid records;
* valid compressed FASTQ input;
* empty FASTQ files;
* empty compressed FASTQ files;
* invalid later records;
* invalid compressed FASTQ input;
* malformed headers occurring in later records.

The test suite is executed using:

```bash
python -m pytest
```

The current observed result is:

```text
13 passed
```

This means that all 13 automated tests passed successfully.

Automated tests provide regression coverage so that changes to the validator can be checked consistently against previously tested behaviour.

---

## 7. Observations and Future Improvements

The expanded validation suite demonstrates that the validator can handle a range of valid and deliberately malformed FASTQ inputs, including compressed input.

The testing process has also identified opportunities for further improvement in diagnostic specificity. For example, the current implementation may report a general incomplete-record error when a specific missing separator could potentially be identified more precisely.

Potential future improvements include:

1. providing more specific error messages for individual structural failures;
2. reporting affected record and line numbers where appropriate;
3. reporting multiple validation errors rather than stopping at the first failure;
4. improving the command-line interface with additional options such as configurable output or validation modes.
