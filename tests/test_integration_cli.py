from quick_calc.cli import run_sequence


def test_full_user_interaction_addition():
    # enter 5, press +, enter 3, press =  => 8
    res = run_sequence(["5", "+", "3", "="])
    assert res.error is None
    assert res.display == "8"


def test_clear_after_calculation_resets_display():
    # 9 * 9 = 81 then Clear => 0
    res = run_sequence(["9", "*", "9", "=", "C"])
    assert res.error is None
    assert res.display == "0"