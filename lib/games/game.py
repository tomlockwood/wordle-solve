import wordle


class Game:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.guess_func = wordle.play

    def run(self):
        self.guesses = []

    def guess(self, word, target):
        guess = self.guess_func(word, target)
        self.guesses.append(guess)
        return guess

    def __str__(self) -> str:
        return f"{self.__name__}(**{self.kwargs})"
