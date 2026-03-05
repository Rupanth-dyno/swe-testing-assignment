from quickcalc.session import QuickCalcSession


def press_many(session: QuickCalcSession, keys: list[str]) -> str:
    display = session.state.display
    for k in keys:
        display = session.press(k)
    return display


def test_full_user_interaction_addition():
    s = QuickCalcSession()
    display = press_many(s, ["5", "+", "3", "="])
    assert display == "8"


def test_clear_resets_after_calculation():
    s = QuickCalcSession()
    press_many(s, ["9", "*", "9", "="])
    assert s.state.display == "81"
    display = press_many(s, ["C"])
    assert display == "0"