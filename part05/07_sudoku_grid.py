def sudoku_grid_correct(sudoku: list):
    for i in range(0, 9):
        row_check = row_correct(sudoku, i)
        col_check = column_correct(sudoku, i)
        if row_check and col_check:
            continue
        else:
            return False
    
    for k in range(0, 9, 3):
        for l in range(0, 9, 3):
            block_check = block_correct(sudoku, k, l)
            if block_check:
                continue
            else:
                return False
    return True


def row_correct(sudoku: list, row_no: int):
    filled = []
    for item in sudoku[row_no]:
        if item > 0 and item in filled:
            return False
        filled.append(item)

    return True


def column_correct(sudoku: list, column_no: int):
    filled = []
    for row in sudoku:
        if row[column_no] > 0 and row[column_no] in filled:
            return False
        filled.append(row[column_no])
    return True


def block_correct(sudoku: list, row_no: int, column_no: int):
    filled = []
    for i in range(row_no, row_no+3):
        for j in range(column_no, column_no + 3):
            item = sudoku[i][j]
            if item > 0 and item in filled:
                return False
            filled.append(item)
    return True