def squared(text, num):
    text = text * num * num
    counter = 0
    start = 0
    while counter < num:
        print(text[start:start+num])
        start += num
        counter += 1

if __name__ == '__main__':
    squared("ab", 3)
    squared("aybabtu", 5)