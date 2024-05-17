def factorials(n: int):
    new_dict = {}
    new_dict[1] = 1
    for i in range(2, n+1):
        new_dict[i] = new_dict[i-1] * i

    return new_dict
    