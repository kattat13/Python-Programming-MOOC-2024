def longest(strings: list):
    longest = ''
    for s in strings:
        if len(s) > len(longest):
            longest = s
    return longest


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
