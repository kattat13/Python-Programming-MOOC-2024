def times_ten(start_index: int, end_index: int):
    new_d = {}
    for i in range(start_index, end_index+1):
        new_d[i] = i * 10
    return new_d