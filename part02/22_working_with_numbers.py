# Write your solution here
nums = []
print('Please type in integer numbers. Type in 0 to finish.')

while True:
    user = int(input('Number:'))
    if user == 0:
        print('Numbers typed in', len(nums))
        print('The sum of the numbers is', sum(nums))
        print('The mean of the numbers is', sum(nums) / len(nums))
        pos_nums = [x for x in nums if x > 0]
        neg_nums = [y for y in nums if y < 0]
        print('Positive numbers', len(pos_nums))
        print('Negative numbers', len(neg_nums))
        break
    else:
        nums.append(user)

