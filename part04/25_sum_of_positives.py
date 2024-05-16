def sum_of_positives(ints: list):
    positives = []
    for n in ints:
        if n > 0:
            positives.append(n)
    return sum(positives)
