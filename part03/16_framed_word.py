word = input('Word:')

w = len(word)
line = '*' * 30
print(line)
if (28 - w) % 2 == 0:
    print('*' + ' ' * int(((28 - w) // 2)) + word + ' ' * int(((28 - w) / 2)) + '*')
else:
    print('*' + ' ' * (int(((28 - w) // 2)) + 1) + word + ' ' * int(((28 - w) / 2)) + '*')
print(line)
