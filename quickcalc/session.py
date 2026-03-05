"""
Quick-Calc: Session Management Module

This module manages the state and user interactions for the Quick-Calc calculator.
It implements a finite state machine that processes user input (digits, operators,
decimal points, equals, and clear) and maintains the calculation session state.

The session layer acts as the bridge between the user interface (CLI) and the
core calculator engine, handling all input validation and state transitions.

Authors: SWE Testing Assignment Team
Version: 1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from quickcalc.calculator import Calculator, DivisionByZeroError


@dataclass
class SessionState:
    """
    Immutable representation of the calculator's current state.
    
    This dataclass encapsulates all necessary state information for the
    calculator session, maintaining a separation of concerns between
    state representation and state manipulation.
    
    Attributes:
        display: The current display string shown to the user. Initially "0".
        _left: The left operand when a binary operation is in progress.
        _op: The current operator (+, -, *, /).
        _typing_new_number: Flag indicating if the next digit starts a new number.
        _error: Error message if an error state has been reached (e.g., "DIV/0").
    """

    display: str = "0"
    _left: Optional[float] = None
    _op: Optional[str] = None
    _typing_new_number: bool = True
    _error: Optional[str] = None

    def clear(self) -> None:
        """
        Reset the session state to initial conditions.
        
        Clears all operational state and resets the display to "0".
        This is called when the user presses the Clear (C) button.
        """
        self.display = "0"
        self._left = None
        self._op = None
        self._typing_new_number = True
        self._error = None

    def __repr__(self) -> str:
        """Return a detailed string representation of the session state."""
        return (
            f"SessionState(display={self.display!r}, left={self._left}, "
            f"op={self._op!r}, typing_new={self._typing_new_number}, "
            f"error={self._error!r})"
        )


class QuickCalcSession:
    """
    Calculator session manager implementing the user interaction flow.
    
    This class manages the complete lifecycle of calculator interaction,
    from initial state to final calculation. It processes user input
    through a method-dispatch pattern and maintains session state.
    
    The session implements calculator behavior similar to standard
    handheld calculators, supporting chained operations and proper
    operator precedence resolution.
    
    Example:
        >>> session = QuickCalcSession()
        >>> session.press("5")
        '5'
        >>> session.press("+")
        '5'
        >>> session.press("3")
        '3'
        >>> session.press("=")
        '8'
    """

    def __init__(self) -> None:
        """Initialize a new calculator session with default state."""
        self.state = SessionState()

    def press(self, key: str) -> str:
        """
        Process a single key press from the user.
        
        This is the main entry point for processing user input. It dispatches
        to appropriate handler methods based on the key type and current state.
        
        Args:
            key: A single character or operator representing user input.
                 Valid inputs: digits (0-9), operators (+, -, *, /),
                 decimal point (.), equals (=), and clear (C).
        
        Returns:
            str: The current display string after processing the key.
        
        Examples:
            >>> session = QuickCalcSession()
            >>> session.press("5")
            '5'
            >>> session.press("0")
            '50'
        
        Note:
            If the calculator is in an error state, only pressing 'C' (clear)
            has any effect.
        """
        key = key.strip()
        
        # Ignore empty input
        if not key:
            return self.state.display

        # In error state, only allow clear operation
        if self.state._error is not None:
            if key.upper() == "C":
                self.state.clear()
            return self.state.display

        # Handle clear operation
        if key.upper() == "C":
            self.state.clear()
            return self.state.display

        # Dispatch to handler based on key type
        if key in "0123456789":
            self._press_digit(key)
        elif key == ".":
            self._press_decimal()
        elif key in {"+", "-", "*", "/"}:
            self._press_operator(key)
        elif key == "=":
            self._press_equals()

        return self.state.display

    def _press_digit(self, digit: str) -> None:
        """
        Handle numeric digit input (0-9).
        
        Updates the display by either starting a new number or appending
        to the current number, with special handling for leading zeros.
        
        Args:
            digit: A single digit character (0-9).
        """
        if self.state._typing_new_number:
            # Start a new number
            self.state.display = digit
            self.state._typing_new_number = False
        else:
            # Append to current number, avoiding leading zeros
            if self.state.display == "0":
                self.state.display = digit
            else:
                self.state.display += digit

    def _press_decimal(self) -> None:
        """
        Handle decimal point input.
        
        Adds a decimal point to the current number. Prevents multiple
        decimal points in a single number and initializes "0." if
        no number is being typed.
        """
        if self.state._typing_new_number:
            self.state.display = "0."
            self.state._typing_new_number = False
        elif "." not in self.state.display:
            # Only add decimal if not already present
            self.state.display += "."

    def _press_operator(self, operator: str) -> None:
        """
        Handle operator input (+, -, *, /).
        
        Processes binary operators. If an operation is already in progress,
        computes the intermediate result before setting the new operator.
        This enables chained operations like "5 + 3 + 2 =".
        
        Args:
            operator: One of: '+', '-', '*', '/'.
        """
        current_value = float(self.state.display)

        # If an operation is pending and we're not starting a new number,
        # compute the intermediate result
        if self.state._op is not None and not self.state._typing_new_number:
            self._compute(current_value)

        # Store the left operand if not already stored
        if self.state._left is None:
            self.state._left = float(self.state.display)

        # Set the operator and prepare for the next operand
        self.state._op = operator
        self.state._typing_new_number = True

    def _press_equals(self) -> None:
        """
        Handle equals button press.
        
        Completes the current operation if one is in progress.
        If no operation is in progress, this has no effect.
        """
        if self.state._op is None or self.state._left is None:
            # No operation in progress
            return
        
        right_value = float(self.state.display)
        self._compute(right_value)
        
        # Clear operation state after computation
        self.state._op = None
        self.state._left = None
        self.state._typing_new_number = True

    def _compute(self, right: float) -> None:
        """
        Compute the result of the current binary operation.
        
        Delegates the actual computation to the Calculator class and updates
        the display with the result. Handles DivisionByZeroError by entering
        an error state.
        
        Args:
            right: The right operand of the operation.
        
        Side Effects:
            Updates self.state.display with the result.
            May update self.state._error if an error occurs.
        """
        assert self.state._op is not None, "No operator set during computation"
        assert self.state._left is not None, "No left operand set during computation"

        left = self.state._left
        op = self.state._op

        try:
            # Perform the calculation based on the operator
            if op == "+":
                result = Calculator.add(left, right)
            elif op == "-":
                result = Calculator.subtract(left, right)
            elif op == "*":
                result = Calculator.multiply(left, right)
            elif op == "/":
                result = Calculator.divide(left, right)
            else:
                # Unknown operator - should never happen
                return

            # Update display with result
            self.state.display = result.as_display()
            self.state._left = float(self.state.display)

        except DivisionByZeroError as e:
            # Enter error state on division by zero
            self.state._error = "DIV/0"
            self.state.display = "DIV/0"