# Wordle Solver

Run with `python wordle_beater.py`.

This hardmode wordle solver takes the following approach:

1. Figure out, for the target list of words, what the frequency of letters per positions 1-5 is.
2. Pick the word that is most likely to get new green letters based on the frequency of letters in each slot.
3. Use the results from the new guess to prune the target list to only words that are possible given all previous guesses.
4. Repeat

# For devs

`./lib/words.py` is a python formatted set of all target words plus all extra possible guesses.

Testing is minimal, run pytest. Tested with python 3.9.