def update_file(finnish_word, english_word):
    with open('dictionary.txt', 'a') as file:
        file.write(f'{finnish_word}:{english_word}\n')
    print('Dictionary entry added')


def read_file():
    words_dict = {}
    with open('dictionary.txt') as file:
        for line in file:
            words_dict[line.split(':')[0]] = line.split(':')[1]
    return words_dict


while True:
    print('1 - Add word, 2 - Search, 3 - Quit')
    choice = input('Function: ')

    if choice == '3':
        print('Bye!')
        break

    if choice == '2':
        search_term = input('Search term: ')
        words = read_file()
        for key, value in words.items():
            if search_term in value or search_term in key:
                print(f'{key} - {value}')


    if choice == '1':
        fin = input('The word in Finnish: ')
        eng = input('The word in English: ')
        update_file(fin, eng)