# Quick-Calc

Quick-Calc is a basic calculator application developed for an Advanced Software Engineering assignment focused on software testing and version control. The application implements the four basic arithmetic operations (addition, subtraction, multiplication, division) with graceful handling of edge cases such as division by zero. It demonstrates professional software development practices including clean code architecture, comprehensive testing, and proper version control.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Rupanth-dyno/swe-testing-assignment.git
cd swe-testing-assignment
```

2. Create a virtual environment (recommended):
```bash
# On Windows:
python -m venv venv
venv\Scripts\activate

# On macOS/Linux:
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the calculator:
```bash
python -m quickcalc.cli
```

## How to Run Tests

All tests are executed with the following command:

```bash
python -m pytest tests/ -v
```

Additional test commands:

```bash
# Run only unit tests
python -m pytest tests/test_unit_calculator.py -v

# Run only integration tests
python -m pytest tests/test_integration_session.py -v

# Run with coverage report
python -m pytest tests/ --cov=quickcalc
```

All 10 tests (8 unit tests and 2 integration tests) pass successfully.

## Testing Framework Research

### Pytest vs Unittest

Python provides two main testing frameworks: Pytest and Unittest. Both are widely used, but they differ in approach and philosophy.

**Pytest Advantages:**
- Simple assertion syntax using plain Python assertions instead of assertEqual() or assertTrue()
- Minimal boilerplate code required; tests are easier to write and read
- Powerful fixture system for setup and teardown operations
- Extensive plugin ecosystem for coverage analysis, mocking, and test parametrization
- Superior error messages that clearly show what failed and why
- Industry standard used by major projects (Django, Flask, Requests)

**Pytest Disadvantages:**
- Requires external installation (not in standard library)
- Slightly higher learning curve for advanced features

**Unittest Advantages:**
- Part of Python standard library, no external dependencies required
- Class-based structure familiar to Java developers (JUnit-like)
- Mature and stable framework

**Unittest Disadvantages:**
- Verbose syntax with required setUp/tearDown methods
- Uses assertion methods like assertEqual() instead of plain assertions
- Limited plugin ecosystem
- More boilerplate code for simple tests

### Why Pytest Was Chosen

Pytest was selected for this project because it provides clean, readable test code with minimal boilerplate. The plain assertion syntax (assert result.value == 8.0) is more intuitive than unittest's assertion methods. Additionally, pytest's fixture system and plugin ecosystem support professional testing practices such as code coverage analysis. Pytest represents the modern Python approach to testing and is the industry standard for contemporary projects.

## Project Structure

```
swe-testing-assignment/
├── quickcalc/
│   ├── __init__.py
│   ├── calculator.py       # Core calculator operations
│   ├── session.py          # Session state management
│   └── cli.py              # Command-line interface
├── tests/
│   ├── test_unit_calculator.py       # 8 unit tests
│   └── test_integration_session.py   # 2 integration tests
├── README.md               # This file
├── TESTING.md              # Testing strategy documentation
├── requirements.txt
├── .gitignore
└── LICENSE
```

## License

This project is licensed under the MIT License. See LICENSE file for details.
