word = input('Please type in a string: ')
word_to_find = input('Please type in a substring: ')

position = word.find(word_to_find)
position2 = word[position+len(word_to_find):].find(word_to_find)

if position == -1 or position2 == -1:
    print('The substring does not occur twice in the string.')
else:
    print(f'The second occurrence of the substring is at index {position2 + position + len(word_to_find)}.')