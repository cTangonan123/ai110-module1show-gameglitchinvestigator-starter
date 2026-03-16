# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
   - This is a simple game in which presents the user with guessing a secret number within an allotted range. It has varying range of difficulties and hints to help assist the user towards selecting the correct secret number.
- [x] Detail which bugs you found.
   - Ranges of difficulty did not reflect levels in expecting that they should increase as difficulty increases
   - Bug in showing hint display in `check_guess` where when a user selects a value above the `secret` value it would present the hint to go higher, vice-versa for when selecting a value below `secret`.
   - `new_game`bug did not allow the user to start a new game, especially after reaching max range of attempts per difficulty.
- [x] Explain what fixes you applied.
   - changed scale of range of values secret can be by refactoring difficulty range in order to account with upper and lower limit.
   - for `check_guess` changed logic so that the hints were displayed properly and associated to the correct conditionals
   - Fixed the `new_game` session button to clear `session_state` whenever the button is selected, where before it only updated certain `session_state` values, resulting in deadlock.


## 📸 Demo

![image of winning guess on game glitch investigator](/scrnli_4eAp2Xv21GtIzi.png)

## 🚀 Stretch Features
- [x] Challenge 1: Advanced Edge-Case Testing

