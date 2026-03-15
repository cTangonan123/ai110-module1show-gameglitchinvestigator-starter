# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  - it looked to be a guessing game that provides the user the option to enter a guess between 1-100
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  - The hints logic would tell me to guess higher even though the actual was lower than the submitted guess
  - a teammate had the opposite occur, telling him to go lower even though the actual was higher that the submitted guess
  - another instance that came up, is that I couldn't start another game after I exhausted my options for the first game.
  - Secret: does not change based off the range designated for difficulty, even when clicking for a new game

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - I used Copilot, Ask mode for inquiry of possible bugs, Plan for evaluating potential routes to fix, and Agent mode for implementation
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - It was correctly able to discern that the check_guess logic was incorrect and that the hint provided would not guide the user towards the correct secret. In order to test I kept the developer debug info open in order to guess below and above secret to see if behavior was as expected.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - It wanted to build an extensive test suite and file when implementing a fix for the newgame bug I had noticed, however I considered it's scope and amount of tests extensive, So i restarted the chat and specified location, and to keep it minimal to account for all direct edge cases. To verify I ran pytest to ensure all existing tests passed before commiting.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - through testing happy case, sad case and potential edge cases, and verifying logic within each test generated
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  - `test_new_game_secret_within_easy_range()` which assimilates a new game and pulls the difficulty range from `get_range_for_difficulty` and asserts the low and high range with easy range.
- Did AI help you design or understand any tests? How?
  - it helped with understanding what I need to test within the dev server to verify, the app as working.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  - because state did not persist across changes
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - streamlit reruns is basically a refresh of a webpage and ultimately clears current state
- What change did you make that finally gave the game a stable secret number?
  - by making sure state persists across changes such as new game.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    - changeing modes, from Ask, to Plan to Agent
- What is one thing you would do differently next time you work with AI on a coding task?
  - be more specific in prompting
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - AI can assist in accelerating understanding.
