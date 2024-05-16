words = []

while True:
    user = input('Word: ')
    if user in words:
        print('You typed in {} different words'.format(len(words)))
        break
    words.append(user)

                 