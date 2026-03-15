# FIX: Refactored all game logic out of app.py into this module using Claude Code Agent mode.

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # FIX: Moved from app.py into logic_utils.py with Claude Code Agent mode so it can be tested independently.
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    # FIX: Moved from app.py into logic_utils.py with Claude Code Agent mode so it can be tested independently.
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # FIX: Moved from app.py and corrected swapped hint messages using Claude Code Agent mode.
    # Original bug: "Too High" showed "Go HIGHER!" and "Too Low" showed "Go LOWER!" — directions were reversed.
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    # FIX: Moved from app.py using Claude Code Agent mode. Removed two bugs:
    # 1. Even-numbered "Too High" guesses were rewarding +5 points instead of deducting.
    # 2. Score had no floor — it could go infinitely negative. Added max(0, ...) to clamp at 0.
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome in ("Too High", "Too Low"):
        return max(0, current_score - 5)

    return current_score
