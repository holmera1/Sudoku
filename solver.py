import pprint

board = [
    [2, 0, 6, 7, 9, 5, 4, 0, 0],
    [7, 0, 0, 2, 0, 0, 8, 0, 0],
    [0, 0, 9, 4, 0, 0, 0, 2, 0],
    [3, 0, 0, 0, 1, 0, 0, 8, 0],
    [8, 0, 0, 3, 4, 2, 6, 1, 5],
    [6, 1, 5, 9, 0, 8, 0, 0, 3],
    [5, 0, 0, 0, 0, 7, 1, 0, 0],
    [9, 0, 3, 0, 2, 4, 0, 0, 0],
    [0, 6, 1, 0, 0, 0, 0, 7, 0]
]

def solve(brd):
    blank = find_blank(brd)
    if not blank:
        return True
    else:
        row, col = blank

    for i in range (1, 10):
        if is_valid(brd, i, (row, col)):
            brd[row][col] = i

            if solve(brd):
                return True

            brd[row][col] = 0
    
    return False


def is_valid(brd, num, pos):

    #check row
    for i in range(len(brd[0])):
        if brd[pos[0]][i] == num and pos[1] != i:
            return False

    #check column
    for i in range(len(brd)):
        if brd[i][pos[1]] == num and pos[0] != i:
            return False

    #check 3x3 box
    xBox = pos[1] // 3
    yBox = pos[0] // 3
    for i in range(yBox*3, yBox*3 + 3):
        for j in range(xBox*3, xBox*3 + 3):
            if brd[i][j] == num and (i, j) != pos:
                return False

    #all 3 tests passsed
    return True


def print_board(brd):
    for i in range(len(brd)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - -")
        for j in range(len(brd[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(brd[i][j])
            else:
                print(str(brd[i][j]) + " ", end="")


def find_blank(brd):
    for i in range(len(brd)):
        for j in range(len(brd[0])):
            if brd[i][j] == 0:
                return (i, j)  #row, col
    return None

print_board(board)
solve(board)
print("solution: ")
print_board(board)