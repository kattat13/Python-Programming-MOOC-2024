def even_numbers(ints : list):
    even = []
    for i in ints:
        if i % 2 == 0:
            even.append(i)
    return even
    