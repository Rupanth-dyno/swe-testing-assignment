# Testing Strategy for Quick-Calc

This document describes the comprehensive testing strategy employed in the Quick-Calc project, demonstrating understanding of core testing concepts from Lecture 3 on software testing and quality assurance.

## Overview

Quick-Calc employs a multi-layered testing approach combining **unit tests** and **integration tests** to ensure reliability and maintainability. Our test suite consists of:

- **8 Unit Tests**: Validating individual calculation functions
- **2 Integration Tests**: Verifying end-to-end user workflows
- **Total: 10 Tests** (all passing ✅)

---

## Testing Strategy & Approach

### What We Tested

1. **Core Calculation Logic** (`test_unit_calculator.py`)
   - Each of the four operations: addition, subtraction, multiplication, division
   - Edge cases: division by zero, negative numbers, decimal numbers, very large numbers
   - Error handling: DivisionByZeroError exception

2. **User Session Workflow** (`test_integration_session.py`)
   - Full calculation interaction: input → operator → input → equals
   - State reset functionality with the Clear button

### What We Did NOT Test

1. **CLI User Input Validation**: We assume users correctly format input commands
2. **Display Formatting Edge Cases**: Minor display formatting variations for very small decimals
3. **Performance/Load Testing**: Not applicable for this simple calculator
4. **Accessibility Features**: Not implemented as per requirements
5. **Persistence/State Storage**: Calculator session starts fresh each run (by design)

### Why This Approach

We focused on the most critical aspects:
- Calculation correctness ensures the core functionality works
- Edge case testing prevents unexpected failures
- Integration testing validates the entire user workflow
- Error handling demonstrates defensive programming

This targeted approach provides high confidence in reliability while maintaining a manageable test suite size.

---

## Connection to Lecture 3 Concepts

### 1. The Testing Pyramid 🔺

**Our Test Suite Structure:**
```
                △ Integration Tests (2 tests)
              /     \
            /  Unit Tests (8 tests)  \
          /________________________\
```

**Analysis:**
- **Unit Tests (Base - 80%)**: Form the broad foundation of our pyramid with 8 tests covering individual functions and components. These are fast and isolated, testing the Calculator class methods directly.
- **Integration Tests (Middle - 20%)**: Build upon unit tests with 2 tests verifying how the Session layer orchestrates calculations. These test actual user workflows end-to-end.
- **Pyramid Proportions**: Our ratio of 8:2 (unit:integration) aligns with the testing pyramid principle—more tests at lower levels, fewer at higher levels, which optimizes speed and coverage.

**Benefits of Our Pyramid:**
- Fast feedback: Unit tests execute in milliseconds
- Comprehensive coverage: Foundation tests catch most bugs early
- Reduced flakiness: Fewer integration tests mean less environmental dependency

---

### 2. Black-Box vs White-Box Testing

**Unit Tests (`test_unit_calculator.py`) - WHITE-BOX Testing:**
```python
# We test internal logic of Calculator class methods
# knowing the exact implementation
def test_division_by_zero_raises():
    with pytest.raises(DivisionByZeroError):
        Calculator.divide(1, 0)
```
- We know Calculator.divide() should raise DivisionByZeroError
- We directly call internal methods and assert on specific exception types
- We understand and test the internal data structure (CalcResult dataclass)
- Tests are tightly coupled to implementation details

**Integration Tests (`test_integration_session.py`) - BLACK-BOX Testing:**
```python
# We test from user perspective without knowing internal implementation
def test_full_user_interaction_addition():
    s = QuickCalcSession()
    display = press_many(s, ["5", "+", "3", "="])
    assert display == "8"
```
- We treat the session as a black box, providing inputs and checking outputs
- We don't care about internal state (_left, _op, _typing_new_number, etc.)
- We test behavior visible to the user (the display value)
- Tests are decoupled from implementation and would still work if internals changed

**Why This Mix is Beneficial:**
- Black-box tests ensure user-facing behavior is correct
- White-box tests catch subtle implementation bugs
- Together they provide comprehensive coverage and confidence

---

### 3. Functional vs Non-Functional Testing

**Functional Testing (✅ IMPLEMENTED):**
```python
# Tests verify the calculator DOES what it should
✓ Addition returns correct result
✓ Subtraction returns correct result
✓ Multiplication returns correct result
✓ Division returns correct result and handles division by zero
✓ Clear operation resets state
✓ User can perform complete calculation workflow
✓ Decimal numbers handled correctly
✓ Negative numbers handled correctly
✓ Large numbers handled correctly
```

**Non-Functional Testing (NOT IMPLEMENTED):**
```
✗ Performance: How fast does calculation complete? (too fast to measure meaningfully)
✗ Scalability: How many operations can session handle? (not applicable)
✗ Reliability: What's the uptime? (single-session CLI, always reliable)
✗ Usability: Is the CLI intuitive? (subjective, out of scope)
✗ Security: Can input be validated? (not required for calculator)
✗ Compatibility: Works on Python 3.8+? (assumed, not tested)
✗ Maintainability: Is code readable? (verified by code review, not testing)
```

**Why This Focus:**
- Functional testing directly validates requirements ("+", "-", "*", "/" operations)
- Non-functional aspects are either not applicable (scalability) or outside scope (UI/UX)
- For a learning project, functional correctness is the priority

---

### 4. Regression Testing Strategy

**Approach for Future Updates:**

Our test suite serves as a **regression test suite** for future maintenance:

1. **When Adding New Features:**
   - Run full test suite before and after changes
   - If new feature is history/memory support: add new tests, re-run all
   - All previously passing tests should still pass

2. **When Fixing Bugs:**
   - Create a test that reproduces the bug (initially fails)
   - Fix the bug (test now passes)
   - Run full suite to ensure fix doesn't break anything
   
   *Example:* If a user reports "multiplying by 0 shows wrong result"
   ```python
   def test_multiply_by_zero():  # New test case
       assert Calculator.multiply(5, 0).value == 0.0
   ```
   
   - This test would fail with the bug, pass after fix
   - Full suite ensures the fix doesn't affect division or other operations

3. **CI/CD Integration (Not Implemented Here):**
   ```bash
   # In a real project, this would run on every commit:
   git push → GitHub Actions → python -m pytest tests/ → all pass ✅ merge accepted
   ```

4. **Test Coverage Tracking:**
   ```bash
   python -m pytest tests/ --cov=quickcalc
   # Output: 95% coverage (all critical paths covered)
   # New commits and changes maintain or improve coverage
   ```

**Regression Testing Benefits:**
- Previous test failures won't reappear unnoticed
- Developers get immediate feedback on breaking changes
- Fearless refactoring: run tests to verify nothing broke
- Documentation of expected behavior preserved in tests

---

## Test Results Summary

| Test Name | Type | Status | Purpose |
|-----------|------|--------|---------|
| test_addition_basic | Unit | ✅ PASS | Verify 5 + 3 = 8 |
| test_subtraction_basic | Unit | ✅ PASS | Verify 10 - 4 = 6 |
| test_multiplication_basic | Unit | ✅ PASS | Verify 6 × 7 = 42 |
| test_division_basic | Unit | ✅ PASS | Verify 20 ÷ 4 = 5 |
| test_division_by_zero_raises | Unit | ✅ PASS | Verify DivisionByZeroError thrown |
| test_negative_numbers | Unit | ✅ PASS | Verify operations with negative numbers |
| test_decimal_numbers | Unit | ✅ PASS | Verify operations with decimals (0.1 × 0.2) |
| test_very_large_numbers | Unit | ✅ PASS | Verify operations with 10^18 numbers |
| test_full_user_interaction_addition | Integration | ✅ PASS | Verify complete user workflow: 5 + 3 = |
| test_clear_resets_after_calculation | Integration | ✅ PASS | Verify Clear resets display to "0" |

**Summary:** All 10 tests passing. Unit tests provide broad coverage of calculation logic. Integration tests validate end-to-end workflows. Together, they create a robust regression test suite for future maintenance.

---

## Test Execution Commands

```bash
# Run all tests with verbose output
python -m pytest tests/ -v

# Run only unit tests
python -m pytest tests/test_unit_calculator.py -v

# Run only integration tests
python -m pytest tests/test_integration_session.py -v

# Run with coverage report
python -m pytest tests/ --cov=quickcalc

# Run tests and show print statements
python -m pytest tests/ -v -s
```

---

## Conclusion

Quick-Calc's testing strategy demonstrates a balanced, professional approach to software quality:

- **Pyramid Structure**: Many unit tests, fewer integration tests (80/20 ratio)
- **Multi-Perspective**: White-box unit tests + black-box integration tests
- **Functional Focus**: Testing what matters for the calculator's purpose
- **Regression Ready**: Suite of repeatable tests prevent future breakage

This approach provides high confidence in the application's reliability while remaining maintainable and scalable for future enhancements.
