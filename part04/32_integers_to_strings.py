def formatted(numbers: list) -> list:
    new_list = []
    for number in numbers:
        new_list.append(f'{number:.2f}')
    return new_list
