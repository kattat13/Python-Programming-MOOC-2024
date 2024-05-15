# Write your solution here
def line(num, text):
    if text:
        print(text[0] * num)
    else:
        print('*' * num)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")