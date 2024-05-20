word = input('Please type in a word: ')
character = input('Please type in a character: ')

position = word.find(character)

if position == -1 or len(word) - position < 3:
    pass
else:
    print(word[position:position+3])