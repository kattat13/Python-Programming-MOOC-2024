def file_to_list():
    words = []
    with open('words.txt') as f:
        for line in f:
            words.append(line.strip())
    return words


def find_words(search_term: str):
    words = file_to_list()
    results = []

    # contains asterisk
    if '*' in search_term:
        if search_term.startswith('*'):
            for word in words:
                if word.endswith(search_term[1:]):
                    results.append(word)
        if search_term.endswith('*'):
            for word in words:
                if word.startswith(search_term[:-1]):
                    results.append(word)

    # contains dot
    if '.' in search_term:
        for word in words:
            if len(word) == len(search_term):
                matching = ''
                for l, k in zip(word, search_term):
                    if k == '.':
                        matching += l
                    elif k != l:
                        break
                    else:
                        matching += l
                if matching == word:
                    results.append(matching)

    # no wildcards
    for word in words:
        if search_term == word:
            results.append(word.strip())
   
    return results


if __name__ == "__main__":
    # print(find_words("*vokes"))
    print(find_words("ca."))