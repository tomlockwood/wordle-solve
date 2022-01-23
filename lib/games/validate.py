import string

zero_alpha = {k: 0 for k in string.ascii_lowercase}
five_alpha = {k: 5 for k in string.ascii_lowercase}

def validate(word, guesses):
    # Get a dict of what letters exist in the word
    word_alphabet = zero_alpha.copy()
    for char in word:
        word_alphabet[char] += 1
    
    for guess in guesses:
        # Set the minimum and max amount of letters for each character
        # That could exist in the word
        alphabet_min = zero_alpha.copy()
        for idx, char in enumerate(guess.pattern):
            validated_word_char = word[idx]
            guess_word_char = guess.word[idx]
            # if the char is green and the word doesn't match, not valid
            if char == 2 and validated_word_char != guess_word_char:
                return False

            # if the char is yellow and the word does match, not valid
            if char == 1 and validated_word_char == guess_word_char:
                return False
            
            # if green or yellow, the alphabet minimum is one more than current
            if char in [2,1]:
                alphabet_min[guess_word_char] += 1
        
        alphabet_max = five_alpha.copy()
        for idx, char in enumerate(guess.pattern):
            guess_word_char = guess.word[idx]
            if char == 0:
                alphabet_min_for_guess_char = alphabet_min[guess_word_char]
                if alphabet_min_for_guess_char > 0:
                    alphabet_max[guess_word_char] = alphabet_min_for_guess_char
                else:
                    alphabet_max[guess_word_char] = 0
        for char, amount in word_alphabet.items():
            if amount > alphabet_max[char]:
                return False
            if amount < alphabet_min[char]:
                return False
    return True