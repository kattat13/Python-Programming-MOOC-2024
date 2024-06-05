def remove_smaller_than(numbers: list, limit: int):
    return [num for num in numbers if num >= limit]