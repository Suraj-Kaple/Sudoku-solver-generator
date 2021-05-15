def row_check(board, row, num):
    if num in board[row]:
        return True
    return False


def col_check(board, col, num):
    for i in range(9):
        if num == board[i][col]:
            return True
    return False


def square_check(board, row, col, num):
    for i in range(3):
        for j in range(3):
            if board[i + row][j + col] == num:
                return True
    return False


def empty_location(board, pos):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                pos[0] = i
                pos[1] = j
                return True
    return False


def check_position(board, row, col, num):
    return not row_check(board, row, num) and not col_check(board, col, num) and not square_check(board, row - row % 3,
                                                                                                  col - col % 3, num)


def sudoku_solver(board):
    pos = [0, 0]

    if not empty_location(board, pos):
        return True
    row = pos[0]
    col = pos[1]

    for num in range(1, 10):
        if check_position(board, row, col, num):
            board[row][col] = num

            if sudoku_solver(board):
                return True

            # failure, unmake & try again
            board[row][col] = 0

    # this triggers backtracking
    return False


grid = [[0 for x in range(9)] for y in range(9)]
grid = [[3, 6, 4, 0, 0, 0, 0, 0, 0],
        [1, 8, 5, 0, 0, 0, 0, 0, 0],
        [9, 7, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 4, 9, 0, 0, 0],
        [0, 0, 0, 1, 8, 2, 0, 0, 0],  # you can enter grid to this code.This is only a sample
        [0, 0, 0, 7, 3, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 3, 5],
        [0, 0, 0, 0, 0, 0, 7, 4, 9],
        [0, 0, 0, 0, 0, 0, 8, 6, 1]]

# if success print the grid
if sudoku_solver(grid):
    for i in range(9):
        if i % 3 == 0:
            print(' - - - - - - - - - - - -')
        for j in range(9):
            if j % 3 == 0:
                print('|', end=' ')
            print(grid[i][j], end=' ')

        print('|')
    print(' - - - - - - - - - - - -')
else:
    print("No solution exists")