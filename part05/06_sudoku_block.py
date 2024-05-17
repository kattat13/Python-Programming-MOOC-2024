def block_correct(sudoku: list, row_no: int, column_no: int):
    filled = []
    for i in range(row_no, row_no+3):
        for j in range(column_no, column_no + 3):
            item = sudoku[i][j]
            if item > 0 and item in filled:
                return False
            filled.append(item)
    return True

