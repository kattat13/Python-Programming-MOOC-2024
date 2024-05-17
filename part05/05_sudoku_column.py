def column_correct(sudoku: list, column_no: int):
    filled = []
    for row in sudoku:
        if row[column_no] > 0 and row[column_no] in filled:
            return False
        filled.append(row[column_no])
    return True