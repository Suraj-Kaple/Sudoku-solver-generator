import random

def empty_location(board,pos):
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                pos[0]=i
                pos[1]=j
                return True
    return False

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


def check_position(board, row, col, num):
    return not row_check(board, row, num) and not col_check(board, col, num) and not square_check(board, row - row % 3,
                                                                                                  col - col % 3, num)


def sudoku_generator(board):
    pos = [0, 0]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(numbers)
    if not empty_location(board, pos):
        return True
    row = pos[0]
    col = pos[1]

    for num in numbers:
        if check_position(board, row, col, num):
            board[row][col] = num

            if sudoku_generator(board):
                return True
            board[row][col] = 0
    return False

grid = [[0 for i in range(9)] for j in range(9)]
if sudoku_generator(grid):
    board=[[0 for i in range(9)] for j in range(9)]
    numb=[0,1,2,3,4,5,6,7,8]
    m=0
    while m<17:
        i=random.choice(numb)
        j=random.choice(numb)
        if board[i][j]==0:
            board[i][j]=grid[i][j]
            m+=1
    for i in range(9):
        print(grid[i])
    print()
    for i in range(9):
        print(board[i])