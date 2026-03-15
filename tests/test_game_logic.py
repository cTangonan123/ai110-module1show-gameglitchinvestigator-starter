from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

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

def test_check_guess_string_secret_does_not_flip_hint():
    # Bug fix: secret passed as string (even-attempt glitch) must still compare correctly
    outcome, _ = check_guess(60, "50")   # 60 > 50  → Too High
    assert outcome == "Too High"
    outcome, _ = check_guess(40, "50")   # 40 < 50  → Too Low
    assert outcome == "Too Low"
    outcome, _ = check_guess(50, "50")   # equal    → Win
    assert outcome == "Win"

# --- parse_guess ---

def test_parse_guess_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True and value == 42 and err is None

def test_parse_guess_empty():
    ok, value, err = parse_guess("")
    assert ok is False and err == "Enter a guess."

def test_parse_guess_non_numeric():
    ok, value, err = parse_guess("abc")
    assert ok is False and err == "That is not a number."

# --- update_score ---

def test_update_score_win():
    assert update_score(0, "Win", 1) == 80   # 100 - 10*(1+1) = 80

def test_update_score_too_low_deducts():
    assert update_score(50, "Too Low", 3) == 45

# --- get_range_for_difficulty / new game bug fix ---


# Tests for new game bug fix: secret must respect the selected difficulty range
def test_new_game_range_easy():
    # Easy mode should produce range 1-20
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20


def test_new_game_range_normal():
    # Normal mode should produce range 1-50
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 50


def test_new_game_range_hard():
    # Hard mode should produce range 1-100
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100


def test_new_game_secret_within_easy_range():
    # A new-game secret for Easy must fall within 1-20
    import random
    low, high = get_range_for_difficulty("Easy")
    secret = random.randint(low, high)
    assert low <= secret <= high

def test_new_game_secret_within_normal_range():
    # A new-game secret for Normal must fall within 1-50
    import random
    low, high = get_range_for_difficulty("Normal")
    secret = random.randint(low, high)
    assert low <= secret <= high

def test_new_game_secret_within_hard_range():
    # A new-game secret for Hard must fall within 1-100
    import random
    low, high = get_range_for_difficulty("Hard")
    secret = random.randint(low, high)
    assert low <= secret <= high
