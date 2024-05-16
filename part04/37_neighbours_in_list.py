def longest_series_of_neighbours(list_of_ints):
    list_of_lengths = []
    series_len = 0
    new_series = True
    for i in range(len(list_of_ints)):
        try:
            diff = abs(list_of_ints[i] - list_of_ints[i+1])
        except IndexError:
            list_of_lengths.append(series_len)
            break
        if diff == 1:
            if new_series:
                series_len = 2
                new_series = False
            else:
                series_len += 1
        else:
            new_series = True
            list_of_lengths.append(series_len)

    return max(list_of_lengths)

    


if __name__ == '__main__':
    my_list = [1, 2, 5, 4, 3, 4]
    print(longest_series_of_neighbours(my_list))