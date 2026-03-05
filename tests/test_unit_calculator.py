import math
import pytest

from quickcalc.calculator import Calculator, DivisionByZeroError


def test_addition_basic():
    assert Calculator.add(5, 3).value == 8.0


def test_subtraction_basic():
    assert Calculator.subtract(10, 4).value == 6.0


def test_multiplication_basic():
    assert Calculator.multiply(6, 7).value == 42.0


def test_division_basic():
    assert Calculator.divide(20, 4).value == 5.0


def test_division_by_zero_raises():
    with pytest.raises(DivisionByZeroError):
        Calculator.divide(1, 0)


def test_negative_numbers():
    assert Calculator.add(-5, -3).value == -8.0
    assert Calculator.subtract(-5, -3).value == -2.0


def test_decimal_numbers():
    assert math.isclose(Calculator.multiply(0.1, 0.2).value, 0.02, rel_tol=1e-9, abs_tol=1e-12)


def test_very_large_numbers():
    big = 10**18
    assert Calculator.add(big, big).value == float(2 * big)