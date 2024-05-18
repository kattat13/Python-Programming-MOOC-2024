# Write your solution here
name = input('Please tell me your name:')

if name == 'Jerry':
    print('Next please!')
else:
    soups = int(input('How many portions of soup?'))
    print(f'The total cost is {soups * 5.90}')
    print('Next please!')