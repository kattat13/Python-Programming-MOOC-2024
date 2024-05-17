def play_turn(game_board: list, x: int, y: int, piece: str):
    if x not in (range(0, 3)) or y not in (range(0, 3)):
        return False
    if game_board[y][x] == '':
        game_board[y][x] = piece
        return True
    return False

if __name__ == '__main__':
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)