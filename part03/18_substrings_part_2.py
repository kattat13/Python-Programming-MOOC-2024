# Write your solution here
user = input('Please type in a string: ')

x = 1
while x <= len(user):
    print(user[-x:])
    x += 1