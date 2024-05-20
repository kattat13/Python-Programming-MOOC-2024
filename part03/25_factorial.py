
while True:
    user = int(input('Please type in a number: '))
    if user <= 0:
        print('Thanks and bye!')
        break
    else:
        counter = 1
        factorial = 1
        while counter <= user:
            factorial *= counter
            counter += 1
        print(f'The factorial of the number {user} is {factorial}')