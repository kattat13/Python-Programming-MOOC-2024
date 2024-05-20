limit = int(input('Limit:'))
n = 2
total = 1
cons_sum = '1'
while total < limit:
    total += n
    cons_sum += f' + {n}'
    n += 1
print(f'The consecutive sum: {cons_sum} = {total}')
