def length_of_longest(words: list) -> int:
    longest = 0
    for word in words:
        if len(word) > longest:
          longest = len(word)

    return longest