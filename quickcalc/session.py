from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from quickcalc.calculator import Calculator, DivisionByZeroError


@dataclass
class SessionState:
    display: str = "0"
    _left: Optional[float] = None
    _op: Optional[str] = None
    _typing_new_number: bool = True
    _error: Optional[str] = None

    def clear(self) -> None:
        self.display = "0"
        self._left = None
        self._op = None
        self._typing_new_number = True
        self._error = None


class QuickCalcSession:
    def __init__(self) -> None:
        self.state = SessionState()

    def press(self, key: str) -> str:
        key = key.strip()
        if not key:
            return self.state.display

        if self.state._error is not None:
            if key.upper() == "C":
                self.state.clear()
            return self.state.display

        if key.upper() == "C":
            self.state.clear()
            return self.state.display

        if key in "0123456789":
            self._press_digit(key)
            return self.state.display

        if key == ".":
            self._press_decimal()
            return self.state.display

        if key in {"+", "-", "*", "/"}:
            self._press_operator(key)
            return self.state.display

        if key == "=":
            self._press_equals()
            return self.state.display

        return self.state.display

    def _press_digit(self, d: str) -> None:
        if self.state._typing_new_number:
            self.state.display = d
            self.state._typing_new_number = False
        else:
            if self.state.display == "0":
                self.state.display = d
            else:
                self.state.display += d

    def _press_decimal(self) -> None:
        if self.state._typing_new_number:
            self.state.display = "0."
            self.state._typing_new_number = False
            return
        if "." not in self.state.display:
            self.state.display += "."

    def _press_operator(self, op: str) -> None:
        current = float(self.state.display)

        if self.state._op is not None and not self.state._typing_new_number:
            self._compute(current)

        if self.state._left is None:
            self.state._left = float(self.state.display)

        self.state._op = op
        self.state._typing_new_number = True

    def _press_equals(self) -> None:
        if self.state._op is None or self.state._left is None:
            return
        right = float(self.state.display)
        self._compute(right)
        self.state._op = None
        self.state._left = None
        self.state._typing_new_number = True

    def _compute(self, right: float) -> None:
        assert self.state._op is not None
        assert self.state._left is not None

        left = self.state._left
        op = self.state._op

        try:
            if op == "+":
                res = Calculator.add(left, right)
            elif op == "-":
                res = Calculator.subtract(left, right)
            elif op == "*":
                res = Calculator.multiply(left, right)
            elif op == "/":
                res = Calculator.divide(left, right)
            else:
                return

            self.state.display = res.as_display()
            self.state._left = float(self.state.display)

        except DivisionByZeroError:
            self.state._error = "DIV/0"
            self.state.display = "DIV/0"