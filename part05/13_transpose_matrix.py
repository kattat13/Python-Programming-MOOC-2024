def transpose(matrix: list):
    new_matrix = []
    for r in matrix:
        new_matrix.append(r[:])

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = new_matrix[j][i]



if __name__ == '__main__':
    matrix = [[1, 2], [1, 2]]
    transpose(matrix)
    print(matrix)