def no_shouting(list_of_strings):
    pruned_list = []
    for s in list_of_strings:
        if not s.isupper():
            pruned_list.append(s)
    return pruned_list


if __name__ == '__main__':
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)