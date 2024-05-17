def add(phone_book):
    name = input('name: ')
    phone = input('number: ')
    if name in phone_book:
        phone_book[name].append(phone)
    else:
        phone_book[name] = [phone]
    print('ok!')


def search(phone_book):
    name = input('name: ')
    if name in phone_book:
        for value in phone_book[name]:
            print(value)
    else:
        print('no number')


def main():
    phone_book = {}
    while True:
        user = int(input('command (1 search, 2 add, 3 quit): '))
        if user == 1:
            search(phone_book)
        if user == 2:
            add(phone_book)
        if user == 3:
            print('quitting...')
            break


main()