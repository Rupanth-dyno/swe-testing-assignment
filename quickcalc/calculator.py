"""
Quick-Calc: Core Calculator Module

This module implements the fundamental arithmetic operations for Quick-Calc.
It provides a clean, type-safe API for performing basic mathematical calculations
with proper error handling and result formatting.

Authors: SWE Testing Assignment Team
Version: 1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Union


class DivisionByZeroError(ZeroDivisionError):
    """
    Exception raised when attempting to divide by zero.
    
    This custom exception extends ZeroDivisionError to provide clear
    signaling of division by zero operations within the calculator context.
    """

    def __init__(self, message: str = "Cannot divide by zero") -> None:
        """Initialize the exception with a descriptive message."""
        super().__init__(message)
        self.message = message


@dataclass(frozen=True)
class CalcResult:
    """
    Immutable result object for calculator operations.
    
    Attributes:
        value: The computed floating-point result of a calculation.
    
    The frozen=True parameter ensures immutability, preventing accidental
    modifications to result values after creation.
    """

    value: float

    def as_display(self) -> str:
        """
        Format the result for display to the user.
        
        Returns:
            str: The value formatted as a string. Integer results are displayed
                 without decimal points (e.g., 8 instead of 8.0).
                 Decimal results retain their decimal representation.
        
        Examples:
            >>> CalcResult(8.0).as_display()
            '8'
            >>> CalcResult(8.5).as_display()
            '8.5'
        """
        if self.value.is_integer():
            return str(int(self.value))
        return str(self.value)

    def __repr__(self) -> str:
        """Return a detailed string representation of the result."""
        return f"CalcResult(value={self.value}, display={self.as_display()!r})"


class Calculator:
    """
    Core calculator engine providing arithmetic operations.
    
    This class implements the four basic arithmetic operations with robust
    error handling. All methods are static and thread-safe.
    """

    @staticmethod
    def add(a: Union[int, float], b: Union[int, float]) -> CalcResult:
        """
        Add two numbers.
        
        Args:
            a: The first operand (int or float).
            b: The second operand (int or float).
        
        Returns:
            CalcResult: An immutable result object containing the sum.
        
        Examples:
            >>> Calculator.add(5, 3).value
            8.0
            >>> Calculator.add(-5, 10).value
            5.0
        """
        result = float(a) + float(b)
        return CalcResult(result)

    @staticmethod
    def subtract(a: Union[int, float], b: Union[int, float]) -> CalcResult:
        """
        Subtract the second number from the first.
        
        Args:
            a: The minuend (int or float).
            b: The subtrahend (int or float).
        
        Returns:
            CalcResult: An immutable result object containing the difference.
        
        Examples:
            >>> Calculator.subtract(10, 4).value
            6.0
            >>> Calculator.subtract(5, 10).value
            -5.0
        """
        result = float(a) - float(b)
        return CalcResult(result)

    @staticmethod
    def multiply(a: Union[int, float], b: Union[int, float]) -> CalcResult:
        """
        Multiply two numbers.
        
        Args:
            a: The first operand (multiplier) (int or float).
            b: The second operand (multiplicand) (int or float).
        
        Returns:
            CalcResult: An immutable result object containing the product.
        
        Examples:
            >>> Calculator.multiply(6, 7).value
            42.0
            >>> Calculator.multiply(0.1, 0.2).value
            0.020000000000000004
        """
        result = float(a) * float(b)
        return CalcResult(result)

    @staticmethod
    def divide(a: Union[int, float], b: Union[int, float]) -> CalcResult:
        """
        Divide the first number by the second.
        
        Performs floating-point division with explicit zero-division checking
        to provide meaningful error messages rather than exceptions.
        
        Args:
            a: The dividend (numerator) (int or float).
            b: The divisor (denominator) (int or float).
        
        Returns:
            CalcResult: An immutable result object containing the quotient.
        
        Raises:
            DivisionByZeroError: If the divisor (b) is zero.
        
        Examples:
            >>> Calculator.divide(20, 4).value
            5.0
            >>> Calculator.divide(10, 3).value
            3.3333...
            >>> Calculator.divide(5, 0)
            Traceback (most recent call last):
                ...
            DivisionByZeroError: Cannot divide by zero
        """
        divisor = float(b)
        if divisor == 0.0:
            raise DivisionByZeroError(
                "Cannot divide by zero. The divisor must be a non-zero number."
            )
        result = float(a) / divisor
        return CalcResult(result)