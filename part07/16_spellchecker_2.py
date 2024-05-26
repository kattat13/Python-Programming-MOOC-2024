from difflib import get_close_matches


user = input('write text: ')

with open('wordlist.txt') as file:
    word_list = []
    for line in file:
        word_list.append(line.strip())

    wrong_words = []
    for word in user.split(' '):
        if word.lower() in word_list:
            print(word, end=' ')
        else:
            print(f'*{word}*', end=' ')
            wrong_words.append(word)

    print('\nsuggestions:')
    for word in wrong_words:
        suggestions = get_close_matches(word, word_list)
        print(f'{word}: {", ".join(suggestions)[:-2]}')

