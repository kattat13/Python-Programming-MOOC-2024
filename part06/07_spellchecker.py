user = input("Write text: ")

with open('wordlist.txt') as file:
    word_list = []
    for line in file:
        word_list.append(line.strip())
    for word in user.split(' '):
        if word.lower() in word_list:
            print(word, end=' ')
        else:
            print(f'*{word}*', end=' ')
