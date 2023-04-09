def can_place_queen(row, col, rows, cols, left_diagonals, right_diagonals):
    if row in rows or col in cols or row - col in left_diagonals or row + col in right_diagonals:
        return False
    return True


def set_queen(row, col, board, rows, cols, left_diagonals, right_diagonals):
    board[row][col] = '*'
    rows.add(row)
    cols.add(col)
    left_diagonals.add(row - col)
    right_diagonals.add(row + col)


def remove_queens(row, col, board, rows, cols, left_diagonals, right_diagonals):
    board[row][col] = '-'
    rows.remove(row)
    cols.remove(col)
    left_diagonals.remove(row - col)
    right_diagonals.remove(row + col)


def put_queens(row, board, rows, cols, left_diagonals, right_diagonals):
    for col in range(8):
        if row == 8:
            for row in board:
                print(' '.join(row))
            print()
            return
        if can_place_queen(row, col, rows, cols, left_diagonals, right_diagonals):
            set_queen(row, col, board, rows, cols, left_diagonals, right_diagonals)
            put_queens(row + 1, board, rows, cols, left_diagonals, right_diagonals)
            remove_queens(row, col, board, rows, cols, left_diagonals, right_diagonals)


board = [['-'] * 8 for _ in range(8)]

put_queens(0, board, set(), set(), set(), set())