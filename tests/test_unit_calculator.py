import pytest
from quick_calc.calculator import Calculator


def test_addition():
    c = Calculator()
    c.input_digit("5")
    c.set_operation("+")
    c.input_digit("3")
    assert c.equals() == 8


def test_subtraction():
    c = Calculator()
    for ch in "10":
        c.input_digit(ch)
    c.set_operation("-")
    c.input_digit("4")
    assert c.equals() == 6


def test_multiplication():
    c = Calculator()
    c.input_digit("6")
    c.set_operation("*")
    c.input_digit("7")
    assert c.equals() == 42


def test_division():
    c = Calculator()
    c.input_digit("8")
    c.set_operation("/")
    c.input_digit("2")
    assert c.equals() == 4


def test_division_by_zero_raises_clear_error():
    c = Calculator()
    c.input_digit("8")
    c.set_operation("/")
    c.input_digit("0")
    with pytest.raises(ZeroDivisionError):
        c.equals()


def test_negative_result_subtraction():
    c = Calculator()
    c.input_digit("3")
    c.set_operation("-")
    for ch in "10":
        c.input_digit(ch)
    assert c.equals() == -7


def test_decimal_addition():
    c = Calculator()
    for ch in "1.5":
        c.input_digit(ch)
    c.set_operation("+")
    for ch in "2.25":
        c.input_digit(ch)
    assert c.equals() == pytest.approx(3.75)


def test_clear_resets_state():
    c = Calculator()
    c.input_digit("9")
    c.set_operation("+")
    c.input_digit("1")
    c.equals()
    c.clear()
    assert c.result == 0.0
    assert c.current_input == ""
    assert c.pending_op is None


def test_large_numbers_multiplication():
    c = Calculator()
    for ch in "90000":
        c.input_digit(ch)
    c.set_operation("*")
    for ch in "90000":
        c.input_digit(ch)
    assert c.equals() == 90000 * 90000