from __future__ import annotations

from dataclasses import dataclass


class DivisionByZeroError(ZeroDivisionError):
    """Raised when attempting to divide by zero in Quick-Calc."""


@dataclass(frozen=True)
class CalcResult:
    value: float

    def as_display(self) -> str:
        if self.value.is_integer():
            return str(int(self.value))
        return str(self.value)


class Calculator:
    @staticmethod
    def add(a: float, b: float) -> CalcResult:
        return CalcResult(float(a) + float(b))

    @staticmethod
    def subtract(a: float, b: float) -> CalcResult:
        return CalcResult(float(a) - float(b))

    @staticmethod
    def multiply(a: float, b: float) -> CalcResult:
        return CalcResult(float(a) * float(b))

    @staticmethod
    def divide(a: float, b: float) -> CalcResult:
        b = float(b)
        if b == 0.0:
            raise DivisionByZeroError("Cannot divide by zero.")
        return CalcResult(float(a) / b)