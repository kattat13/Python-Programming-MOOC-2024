def file_content():
    content_as_list = []
    with open('matrix.txt') as file:
        for line in file:
            for element in line.split(','):
                content_as_list.append(int(element))
    return content_as_list


def matrix_sum():
    content = file_content()
    return sum(content)


def matrix_max():
    content = file_content()
    return max(content)


def row_sums():
    list_of_sums = []
    with open('matrix.txt') as file:
        for line in file:
            element_sum = 0
            for element in line.split(','):
                element_sum += int(element)
            list_of_sums.append(element_sum)
    return list_of_sums