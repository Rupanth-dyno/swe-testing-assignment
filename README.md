# Quick-Calc (Software Engineering & Testing Assignment)

Quick-Calc is a simple calculator application built for an Advanced Software Engineering assignment focused on **software testing** and **version control**. It provides a command-line interface for performing basic arithmetic operations with comprehensive unit and integration tests to demonstrate professional testing practices.

## Features
- **Addition**: Add two numbers
- **Subtraction**: Subtract two numbers
- **Multiplication**: Multiply two numbers
- **Division**: Divide two numbers with graceful division by zero handling
- **Clear**: Reset the calculator state
- **Comprehensive Test Suite**: 10+ tests covering unit, integration, edge cases, and error handling

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Rupanth-dyno/swe-testing-assignment.git
cd swe-testing-assignment
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the calculator
```bash
python -m quickcalc.cli
```

Example usage:
```
> 5 + 3 =
Display: 8
> 10 - 4 =
Display: 6
> C
Display: 0
```

## How to Run Tests

All tests are implemented using **pytest** and can be executed with a single command:

```bash
# Run all tests
python -m pytest tests/ -v

# Run only unit tests
python -m pytest tests/test_unit_calculator.py -v

# Run only integration tests
python -m pytest tests/test_integration_session.py -v

# Run with coverage report
python -m pytest tests/ --cov=quickcalc
```

**Test Results Summary:**
- Total Tests: 10
- Unit Tests: 8
- Integration Tests: 2
- All tests: ✅ PASSING

## Testing Framework Research

### Pytest vs Unittest

**Pytest:**
- **Advantages**: Simple syntax with pure Python assertions, minimal boilerplate, powerful fixtures for setup/teardown, excellent plugin ecosystem, detailed failure reporting
- **Disadvantages**: Requires installation, slightly slower than unittest for large test suites
- **Use case**: Modern Python projects, complex testing scenarios, projects needing plugins (coverage, mocking, etc.)

**Unittest:**
- **Advantages**: Part of Python standard library, no external dependencies, class-based structure for organizational purposes
- **Disadvantages**: Verbose syntax with assertEqual/assertTrue methods, requires more boilerplate, less intuitive assertion messages
- **Use case**: Simple projects, environments with strict dependency restrictions

**Final Choice: Pytest**

We chose **Pytest** for this project because:
1. It provides cleaner, more readable test code with simple assertions
2. The pip ecosystem includes excellent plugins like `pytest-cov` for coverage analysis
3. The failure output is more descriptive and helpful for debugging
4. Its fixture system makes test setup/teardown elegant and reusable
5. It's the industry standard for modern Python projects

## Project Structure

```
swe-testing-assignment/
├── quickcalc/              # Main application package
│   ├── __init__.py
│   ├── calculator.py       # Core calculation logic
│   ├── session.py          # Session state and user input handling
│   └── cli.py              # Command-line interface
├── tests/                  # Test suite
│   ├── test_unit_calculator.py       # Unit tests for Calculator class
│   └── test_integration_session.py   # Integration tests for QuickCalcSession
├── requirements.txt        # Project dependencies
├── README.md              # This file
├── TESTING.md             # Testing strategy and documentation
└── LICENSE                # MIT License
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
