def shortest(words: list) -> int:
    best = words[0]
    for word in words:
        if len(word) < len(best):
          best = word

    return best