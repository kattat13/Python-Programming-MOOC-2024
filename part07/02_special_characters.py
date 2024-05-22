import string


def separate_characters(my_string: str):
    ascii_letters = []
    punctuations = []
    others = []
    for char in my_string:
        if char in string.ascii_letters:
            ascii_letters.append(char)
        elif char in string.punctuation:
            punctuations.append(char)
        else:
            others.append(char)

    return ''.join(ascii_letters), ''.join(punctuations), ''.join(others)