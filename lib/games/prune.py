from .validate import validate


def prune_wordlist(guesses, wordlist) -> set:
    if len(guesses) == 0:
        return wordlist
    guess_words = [guess.word for guess in guesses]

    possibles = set()

    for word in wordlist:
        if word in guess_words:
            continue
        if validate(word, guesses):
            possibles.add(word)

    return possibles
