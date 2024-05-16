def everything_reversed(words: list):
    new_list = []
    for word in words[::-1]:
        new_list.append(word[::-1])

    return new_list


if __name__ == '__main__':
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)