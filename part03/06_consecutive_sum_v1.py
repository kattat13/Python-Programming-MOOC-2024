# Write your solution here
limit = int(input('Limit:'))
x = 1
calc_sum = 0
while calc_sum < limit:
    # print('sum is', calc_sum)
    calc_sum += x
    # print('sum is', calc_sum)
    x += 1
    # print('new x is', x, '\n')
print(calc_sum)