user = int(input('Please type in a number: '))

a = 1
b = 1
while a <= user:
    while b <= user:
        print(f'{a} x {b} = {a * b}')
        b += 1
    else:
        b = 1
    a += 1
