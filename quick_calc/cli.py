from __future__ import annotations

from dataclasses import dataclass
from quick_calc.calculator import Calculator


@dataclass
class CLIResult:
    display: str
    error: str | None = None


def run_sequence(tokens: list[str]) -> CLIResult:
    """
    Simulate a user interaction sequence (like pressing calculator buttons).

    Allowed tokens:
    - digits (e.g., "5", "12")
    - "." (or included inside a number token like "1.5")
    - "+", "-", "*", "/"
    - "="
    - "C" (clear)

    Example:
      ["5", "+", "3", "="] -> display "8"
    """
    calc = Calculator()

    def display_value() -> str:
        if calc.current_input != "":
            return calc.current_input
        if calc.result.is_integer():
            return str(int(calc.result))
        return str(calc.result)

    for t in tokens:
        if t == "C":
            calc.clear()
            continue

        if t in {"+", "-", "*", "/"}:
            calc.set_operation(t)
            continue

        if t == "=":
            try:
                calc.equals()
            except ZeroDivisionError as e:
                # Graceful handling: show error and reset display to "0"
                calc.clear()
                return CLIResult(display="0", error=str(e))
            continue

        # allow multi-char numeric tokens like "12" or "1.5"
        for ch in t:
            calc.input_digit(ch)

    return CLIResult(display=display_value(), error=None)