
def add_numbers_to_list(numbers: list):
    while len(numbers) % 5 != 0:
        numbers.append(numbers[-1] + 1)
        add_numbers_to_list(numbers)


if __name__ == '__main__':
    numbers = [1, 2]
    add_numbers_to_list(numbers)
    print(numbers)


