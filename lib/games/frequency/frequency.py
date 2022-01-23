from ..game import Game
from ..prune import prune_wordlist
from ...words import targetlist, guesslist
import string

zero_alpha = {k: 0 for k in string.ascii_lowercase}


def make_indexes() -> dict:
    return {k + 1: zero_alpha.copy() for k in range(5)}


class FrequencyGame(Game):
    def __init__(self, **kwargs):
        expanded_list_guesses = kwargs.get("expanded_list_guesses")
        if not expanded_list_guesses and not expanded_list_guesses == 0:
            expanded_list_guesses = 2
        kwargs["expanded_list_guesses"] = expanded_list_guesses
        self.expanded_list_guesses = expanded_list_guesses
        super().__init__(**kwargs)

    def __str__(self):
        return super().__str__()

    def letter_frequency_in_position(self, wordlist) -> dict:
        indexes = make_indexes()

        for word in wordlist:
            for idx, letter in enumerate(word):
                indexes[idx + 1][letter] += 1

        return indexes

    def get_candidate(self, possible_guesses) -> str:
        """
        Return best candidate for next guess.
        """

        indexes = self.letter_frequency_in_position(self.targetlist)

        max_word = ""
        max_word_score = 0

        for word in possible_guesses:
            word_score = 0
            for idx, letter in enumerate(word):
                word_score += indexes[idx + 1][letter]
            if word_score > max_word_score:
                max_word_score = word_score
                max_word = word
        return max_word, max_word_score

    def run(self, target):
        super().run()
        self.targetlist = targetlist
        self.guesslist = set.union(targetlist, guesslist)
        for _ in range(self.expanded_list_guesses):
            self.targetlist = prune_wordlist(self.guesses, self.targetlist)
            self.guesslist = prune_wordlist(self.guesses, self.guesslist)
            candidate, score = self.get_candidate(self.guesslist)
            guess = self.guess(candidate, target)
            if guess.won:
                return
        self.targetlist = targetlist
        for _ in range(6 - self.expanded_list_guesses):
            self.targetlist = prune_wordlist(self.guesses, self.targetlist)
            candidate, score = self.get_candidate(self.targetlist)
            guess = self.guess(candidate, target)
            if guess.won:
                return
