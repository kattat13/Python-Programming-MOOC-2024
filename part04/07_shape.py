def line(num, text):
    if text:
        print(text[0] * num)
    else:
        print('*' * num)


def triangle(size, character):
    i = 1
    while i <= size:
        line(i, character)
        i += 1


def shape(triangle_size, triangle_char, rectangle_size, rectangle_char):
    triangle(triangle_size, triangle_char)
    for x in range(rectangle_size):
        line(triangle_size, rectangle_char)



# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")