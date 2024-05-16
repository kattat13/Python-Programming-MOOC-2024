def most_common_character(word: str):
    most_common = 0
    best = ''
    for letter in word:
        if word.count(letter) > most_common:
            most_common = word.count(letter)
            best = letter
    return best


if __name__ == '__main__':
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))