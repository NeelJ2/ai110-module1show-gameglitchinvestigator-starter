import pytest
from logic_utils import check_guess, update_score, parse_guess, get_range_for_difficulty


# --- check_guess ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_message():
    _, message = check_guess(60, 50)
    assert "LOWER" in message

def test_too_low_message():
    _, message = check_guess(40, 50)
    assert "HIGHER" in message

def test_win_message():
    _, message = check_guess(50, 50)
    assert "Correct" in message


# --- update_score ---

def test_win_first_attempt_gives_max_points():
    # attempt_number=1: 100 - 10*(1+1) = 80
    score = update_score(0, "Win", 1)
    assert score == 80

def test_win_score_never_below_10_points():
    # attempt_number=10: 100 - 10*11 = -10 → clamped to 10
    score = update_score(0, "Win", 10)
    assert score == 10

def test_wrong_guess_deducts_5():
    score = update_score(20, "Too High", 1)
    assert score == 15

def test_score_floors_at_zero():
    score = update_score(3, "Too Low", 1)
    assert score == 0

def test_unknown_outcome_unchanged():
    score = update_score(50, "Unknown", 1)
    assert score == 50


# --- parse_guess ---

def test_parse_valid_int():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_float_string_truncates():
    ok, value, err = parse_guess("7.9")
    assert ok is True
    assert value == 7

def test_parse_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None

def test_parse_none():
    ok, value, err = parse_guess(None)
    assert ok is False

def test_parse_non_numeric():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert err is not None

def test_parse_negative_number():
    ok, value, err = parse_guess("-5")
    assert ok is True
    assert value == -5


# --- get_range_for_difficulty ---

def test_easy_range():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_normal_range():
    assert get_range_for_difficulty("Normal") == (1, 100)

def test_hard_range():
    assert get_range_for_difficulty("Hard") == (1, 50)

def test_unknown_difficulty_defaults():
    assert get_range_for_difficulty("Unknown") == (1, 100)
