word = input('Please type in a word: ')
character = input('Please type in a character: ')


while True:
    position = word.find(character)
    if position == -1 or len(word) - position < 3:
        break
    print(word[position:position+3])
    word = word[position+1:]