from __future__ import annotations

class Calculator:
    """
    Core calculation logic for Quick-Calc.

    Supports:
    - Addition (+)
    - Subtraction (-)
    - Multiplication (*)
    - Division (/) with division-by-zero handling
    - Clear (C) via clear()
    """

    def __init__(self) -> None:
        self.clear()

    def clear(self) -> None:
        self.current_input: str = ""
        self.result: float = 0.0
        self.pending_op: str | None = None
        self._has_result: bool = False

    def input_digit(self, ch: str) -> None:
        """Accept digits or '.' to build the current number."""
        if ch not in "0123456789.":
            raise ValueError("Only digits and '.' are allowed.")
        # prevent multiple decimals
        if ch == "." and "." in self.current_input:
            return
        self.current_input += ch

    def set_operation(self, op: str) -> None:
        """Set the pending operation. If a number is currently input, fold it into result."""
        if op not in {"+", "-", "*", "/"}:
            raise ValueError("Unsupported operation.")

        if self.current_input != "":
            num = float(self.current_input)
            if not self._has_result:
                self.result = num
                self._has_result = True
            elif self.pending_op is not None:
                self.result = self._apply(self.result, num, self.pending_op)
            self.current_input = ""

        self.pending_op = op

    def equals(self) -> float:
        """Compute result using pending operation and current input (if present)."""
        if self.pending_op is None:
            if self.current_input != "":
                self.result = float(self.current_input)
                self._has_result = True
                self.current_input = ""
            return self.result

        if self.current_input == "":
            # pressing "=" without a second operand: treat as no-op
            return self.result

        num = float(self.current_input)
        self.result = self._apply(self.result, num, self.pending_op)
        self.current_input = ""
        self.pending_op = None
        self._has_result = True
        return self.result

    @staticmethod
    def _apply(a: float, b: float, op: str) -> float:
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*":
            return a * b
        if op == "/":
            if b == 0:
                # “Graceful”: raise a clear error for the UI/input layer to handle
                raise ZeroDivisionError("Cannot divide by zero.")
            return a / b
        raise ValueError("Unsupported operation.")