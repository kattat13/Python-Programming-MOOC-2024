while True:
    print('1 - add an entry, 2 - read entries, 0 - quit')
    user_choice = input('Function: ')

    if user_choice == '1':
        entry = input('Diary entry: ')
        with open('diary.txt', 'a') as f:
            f.write(f'{entry}\n')
        print('Diary saved')
        print()
    
    elif user_choice == '2':
        print('Entries:')
        with open('diary.txt', 'r') as f:
            for line in f:
                print(line)
    
    else:
        print('Bye now!')
        break
