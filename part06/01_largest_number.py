def largest():
    with open('numbers.txt') as file:
        largest_number = 0
        for line in file:
            if int(line) > largest_number:
                largest_number = int(line)
    return largest_number