# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  There was a gray screen with an entry for a input for a number. There were 3 buttons and a attempt counter.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  1. Pressing enter to submit a guess didn't work
  2. New game didn't work.
  3. Hint never showed up.
  4. Even it did at the end, the hint was off (lower even tho the number was lower than the actual number).
  5. It wasn't from 0 to 100.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
    AI was able to show me that there was an issue with the parse guess. Although the range was correct, in the actual check guess there was no real enforcing of the boundaries.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  When trying to run the code AFTER the logic was extracted into logic_utils, the AI (or maybe me haha) didn't account for a type mismatch.

  TypeError: '>' not supported between instances of 'int' and 'str'
Traceback:
File "/Users/gliccolo/ai110-module1show-gameglitchinvestigator-starter/app.py", line 145, in <module>
    outcome, message = check_guess(guess_int, secret)
                       ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
File "/Users/gliccolo/ai110-module1show-gameglitchinvestigator-starter/logic_utils.py", line 24, in check_guess
    if guess > secret:
       ^^^^^^^^^^^^^^
  
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - I tried to redo the same issue that cause a break in the logic of the code. For example in normal mode I tried guessing with a negative number and the hints worked properly.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
    The two tests that AI and I wrote were about
    test_too_high_message — guess of 60 vs secret 50 must return a message containing "LOWER"
    test_too_low_message — guess of 40 vs secret 50 must return a message containing "HIGHER"
- Did AI help you design or understand any tests? How?
    Yes!! It helped me understand the pytest syntax and how it works. I had it explain me the concepts in "laymen's terms".
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit reruns I essentially win a new change in the code or new command is executed and then it starts back up again from the top and a session state is how a website can keep track of the changes in the website and in this case, the session state was never update the app originally, and it was also set to a wrong value.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
   I think I did a good job of trying to understand the code before I go ahead and use AI to make any changes of a note of what was broken and also just testing out what was broken to use my intuition to figure it out.
- What is one thing you would do differently next time you work with AI on a coding task?
  I didn't really use it after he's changed so next time I would commit after each change so that I can keep a nice track and also be able to go back if things break too badly. Prompting lies and testing lies. I should have ask more about the code that was written a bit more.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  This project helped me understand how to gradually use AI to implement changes rather than having AI do all the work. I think the biggest issue with AI is, when you have it drive for you instead of you being in the driver seat. Being able to a mock incremental progression of logic that you would have when you work without AI helps you understand the code but be able to work efficiently.
