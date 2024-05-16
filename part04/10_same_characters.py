def same_chars(text, num1, num2):
    try:
        char1 = text[num1]
        char2 = text[num2]
        if char1 == char2:
            return True
        else:
            return False
    except IndexError:
        return False



# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 28))