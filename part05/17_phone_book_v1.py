phone_book = {}

while True:
    user = int(input('command (1 search, 2 add, 3 quit) '))

    if user == 2:
        name = input('name: ')
        phone = input('number: ')
        phone_book[name] = phone
        print('ok!')
    
    elif user == 1:
        name = input('name: ')
        if name in phone_book:
            print(phone_book[name])
        else:
            print('no number')
    
    else:
        print('quitting...')
        break