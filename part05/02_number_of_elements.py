def count_matching_elements(my_matrix: list, element: int):
    matches_count = 0
    for row in my_matrix:
        for item in row:
            if item == element:
                matches_count += 1

    return matches_count


if __name__ == '__main__':
    print(count_matching_elements([[1, 2, 3], [2, 3, 1], [4, 5, 6]], 2))