import string


zero_alpha = {k: 0 for k in string.ascii_lowercase}


class Guess:
    def __init__(self, word, pattern):
        """
        2 = Green
        1 = Yellow
        0 = Miss
        """
        self.word = word

        self.pattern = pattern

    @property
    def pattern_string(self):
        return "".join([str(x) for x in self.pattern])

    @property
    def won(self):
        return self.pattern_string == "22222"

    def __repr__(self):
        return f"{self.word}: {self.pattern_string}"


def play(guess, target) -> Guess:
    pattern = [0, 0, 0, 0, 0]
    target_alphabet = zero_alpha.copy()
    for char in target:
        target_alphabet[char] += 1

    for idx, char in enumerate(guess):
        if char == target[idx]:
            pattern[idx] = 2
            target_alphabet[char] -= 1

    for idx, char in enumerate(guess):
        if target_alphabet[char] > 0 and pattern[idx] != 2:
            pattern[idx] = 1
            target_alphabet[char] -= 1

    return Guess(guess, pattern)
