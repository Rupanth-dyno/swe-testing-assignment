"""
Quick-Calc: Command-Line Interface Module

This module provides a user-friendly command-line interface for the Quick-Calc
calculator application. It handles all user interaction, input validation,
and display formatting.

The CLI is designed for simplicity and ease of use, supporting both basic
and advanced calculator operations.

Authors: SWE Testing Assignment Team
Version: 1.0.0
"""

from __future__ import annotations

import sys

from quickcalc.session import QuickCalcSession


def print_header() -> None:
    """Print the application header and welcome message."""
    print("=" * 60)
    print("  QUICK-CALC v1.0.0 - Advanced Calculator")
    print("  Software Engineering & Testing Assignment")
    print("=" * 60)
    print()


def print_help() -> None:
    """Display comprehensive help information for calculator usage."""
    help_text = """
QUICK-CALC USAGE GUIDE
──────────────────────

OPERATIONS:
  • Addition:       Enter operands separated by '+' (e.g., 5 + 3 =)
  • Subtraction:    Enter operands separated by '-' (e.g., 10 - 4 =)
  • Multiplication: Enter operands separated by '*' (e.g., 6 * 7 =)
  • Division:       Enter operands separated by '/' (e.g., 20 / 4 =)
  • Clear:          Press 'C' to reset the calculator
  • Decimal:        Use '.' for decimal numbers (e.g., 3.14)

EXAMPLES:
  5 + 3 =           → 8
  10 * 2 - 5 =      → 15
  100 / 3.5 =       → 28.571...
  C                 → Clears display
  5 / 0             → Error: DIV/0

COMMAND SYNTAX:
  Enter multiple keys separated by spaces on a single line.
  Examples:
    > 5 + 3 =
    > 100 * 2 - 50 =
    > 7 . 5 + 2 . 5 =

SPECIAL COMMANDS:
  help              Display this help message
  clear             Clear the calculator display
  quit / exit       Exit the calculator

NOTES:
  • Decimal numbers are supported (e.g., 3.14159)
  • Chained operations are supported (e.g., 5 + 3 + 2 =)
  • Division by zero is handled gracefully
  • After an error, press 'C' to clear the error state

"""
    print(help_text)


def print_instructions() -> None:
    """Print quick instructions for the user."""
    instructions = """
INSTRUCTIONS:
  Enter numbers and operators separated by spaces.
  Type 'help' for detailed usage information.
  Type 'quit' or 'exit' to exit the calculator.
  
EXAMPLE SESSION:
  > 5 + 3 =
  Display: 8
  
"""
    print(instructions)


def main() -> None:
    """
    Main entry point for the Quick-Calc CLI application.
    
    Manages the interactive session loop, processing user input and
    displaying results until the user exits.
    """
    # Initialize the calculator session
    session = QuickCalcSession()
    
    # Display welcome information
    print_header()
    print_instructions()
    print(f"Display: {session.state.display}\n")

    # Main interaction loop
    while True:
        try:
            # Get user input
            user_input = input(">>> ").strip()
            
            # Handle empty input
            if not user_input:
                continue
            
            # Handle special commands
            if user_input.lower() in ("quit", "exit"):
                print("\n✓ Thank you for using Quick-Calc. Goodbye!")
                break
            
            if user_input.lower() == "help":
                print_help()
                continue
            
            if user_input.lower() == "clear":
                session.state.clear()
                print(f"Display: {session.state.display}")
                continue
            
            # Process calculator input
            display_result = None
            for key in user_input.split():
                display_result = session.press(key)
            
            # Display the result
            if display_result is not None:
                print(f"Display: {display_result}")
        
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\n✓ Calculator closed. Goodbye!")
            sys.exit(0)
        
        except ValueError as e:
            # Handle invalid numeric input
            print(f"✗ Error: Invalid input. Please enter valid numbers and operators.")
            print(f"  Hint: Type 'help' for usage instructions.")
        
        except Exception as e:
            # Handle unexpected errors
            print(f"✗ Unexpected error: {type(e).__name__}: {e}")
            print(f"  Please try again or type 'help' for assistance.")


if __name__ == "__main__":
    main()