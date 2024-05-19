# Write your solution here
password = input('Password')
while True:
    next_pass = input('Repeat password')
    if next_pass != password:
        print('They do not match!')
    else:
        print('User account created!')
        break