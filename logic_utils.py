# FIX: Refactored difficulty range so logic is constiently expanding across difficulties.
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100

# FIX: Refactored simplified parsing logic
def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."
    try:
        value = int(float(raw)) if "." in raw else int(raw)
    except Exception:
        return False, None, "That is not a number."
    return True, value, None

# FIX: Refactored check_guess to properly to assign correct hints based on logical guess
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # Normalize both values to int to avoid string-vs-int comparison bugs
    try:
        guess = int(guess)
        secret = int(secret)
    except (TypeError, ValueError):
        pass

    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"

# FIX: Refactored update_score simplified logic for win scenario using max(), one lined Too high and Too low scenarios.
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = max(100 - 10 * (attempt_number + 1), 10)
        return current_score + points
    if outcome == "Too High":
        return current_score + 5 if attempt_number % 2 == 0 else current_score - 5
    if outcome == "Too Low":
        return current_score - 5
    return current_score
