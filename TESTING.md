# Testing Strategy for Quick-Calc

This document explains the testing approach used in the Quick-Calc project and how it relates to software testing concepts from Lecture 3.

---

## Testing Strategy

The Quick-Calc project uses a combination of **unit testing** and **integration testing** to ensure that the calculator works correctly.

### Unit Testing
Unit tests focus on testing the **core calculation logic** in isolation.  
The tests verify that each operation behaves correctly:

- Addition
- Subtraction
- Multiplication
- Division
- Handling division by zero
- Negative numbers
- Decimal calculations
- Very large numbers
- Resetting calculator state using the clear function

These tests ensure that the internal logic of the calculator works correctly.

### Integration Testing
Integration tests verify that the **user input layer interacts correctly with the calculator logic**.

Examples tested:
- Simulating a full interaction: `5 + 3 = 8`
- Verifying that pressing **Clear (C)** resets the display to `0`

This confirms that the input interface and calculation engine work together correctly.

---

## Lecture Concepts Applied

### Testing Pyramid
The testing approach follows the **Testing Pyramid** principle:

- **Many unit tests** verify core functionality quickly.
- **Fewer integration tests** verify interactions between system components.

This keeps tests fast and reliable while still verifying overall behavior.

---

### Black-Box vs White-Box Testing

**White-box testing** was used in unit tests because the internal functions of the calculator were directly tested.

**Black-box testing** was used in integration tests because the system was tested from the user's perspective without focusing on internal implementation.

---

### Functional vs Non-Functional Testing

This project focuses primarily on **functional testing**, ensuring that the calculator produces correct results for each operation.

Non-functional testing such as performance or security testing was not included because the application is small and does not require heavy system resources.

---

### Regression Testing

The test suite can also be used for **regression testing**.  
Whenever the code is updated or new features are added, the test suite can be executed to verify that existing functionality has not been broken.

---

## Test Results Summary

All tests can be executed using:

| Test Name | Type | Result |
|----------|------|--------|
| test_addition | Unit | Pass |
| test_subtraction | Unit | Pass |
| test_multiplication | Unit | Pass |
| test_division | Unit | Pass |
| test_division_by_zero | Unit | Pass |
| test_negative_result | Unit | Pass |
| test_decimal_addition | Unit | Pass |
| test_clear_resets_state | Unit | Pass |
| test_large_numbers | Unit | Pass |
| test_full_user_interaction | Integration | Pass |
| test_clear_function | Integration | Pass |
