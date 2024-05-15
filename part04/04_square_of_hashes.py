def line(num, text):
    if text:
        print(text[0] * num)
    else:
        print('*' * num)

def square_of_hashes(size):
    i = 0
    while i < size:
        line(size, "#")
        i += 1 

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
