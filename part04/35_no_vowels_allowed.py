def no_vowels(word):
    new_word = ''
    for letter in word:
        if letter not in ('a', 'e', 'i', 'o', 'u'):
            new_word += letter

    return new_word


if __name__ == '__main__':
    my_string = "this is an example"
    print(no_vowels(my_string))