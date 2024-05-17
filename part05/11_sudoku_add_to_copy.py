from copy import deepcopy

def print_sudoku(sudoku: list):
    for i, row in enumerate(sudoku):

        for j, item in enumerate(row):
            if item == 0:
                print('_ ', end='')
            else:
                print(str(item) + ' ', end='')
            if (j+1) % 3 == 0:
                print(' ', end='')
        if (i+1) % 3 == 0:
            print()
        print()


def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_sudoku = []
    for r in sudoku:
        new_sudoku.append(r[:])
    new_sudoku[row_no][column_no] = number
    return new_sudoku


if __name__ == '__main__':

    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)