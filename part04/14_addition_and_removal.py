lst = []


while True:
    print('The list is now', lst)
    user = input('a(d)d, (r)emove or e(x)it: ')
    if user == 'd':
        if not lst:
            lst.append(1)
        else:            
            lst.append(lst[-1]+1)
    elif user == 'r':
        last = len(lst) - 1
        lst.pop(last)
    else:
        print('Bye!')
        break
