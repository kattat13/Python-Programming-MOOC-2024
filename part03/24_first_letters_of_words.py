sentence = input('Please type in a sentence: ')

words = sentence.split(' ')
for word in words:
    print(word[0])