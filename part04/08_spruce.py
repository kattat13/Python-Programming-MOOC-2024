# Write your solution here
def spruce(size):
    print('a spruce!')
    char = '*'
    i = 1
    j = 1

    while i <= size:
        print(f'{" " * (size - i)}{char * (j)}')
        i += 1
        j += 2
    print(f'{" " * (size - 1)}{char}')    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)