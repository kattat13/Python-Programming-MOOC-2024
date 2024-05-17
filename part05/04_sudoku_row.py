def row_correct(sudoku: list, row_no: int):
    filled = []
    for item in sudoku[row_no]:
        if item > 0 and item in filled:
            return False
        filled.append(item)

    return True