def histogram(word: str):
    letters = {}
    for letter in word:
        # initialize if letter not in letters:
        if letter not in letters:
            letters[letter] = 0
        letters[letter] += 1

    for key, value in letters.items():
        stars = '*' * value
        print(f'{key} {stars}')
        