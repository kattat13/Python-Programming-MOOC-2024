user = int(input('Please type in a number: '))

a = 1
while a < user:
    if a + 1 <= user:
        print(a + 1)
    print(a)
    a += 2
if user % 2 == 1:
    print(user)