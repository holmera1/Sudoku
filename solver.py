import pprint

#sudoku board to be solved - can be changed, will notify if unsolvable
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

#dimensions of all sudoku boards are 9x9
dim = 9

#prints the sudoku board in the terminal
def print_board(board):
    for i in range(dim):

        #adds lines to separate 3x3 boxes
        if i % 3 == 0 and i != 0:   
            print("---------------------")

        for j in range(dim):

            #adds lines to separate 3x3 boxes
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            #prints last column of numbers without extra space
            if j == 8:
                print(board[i][j])

            #prints columns of numbers with extra space
            else:
                print(str(board[i][j]) + " ", end="")


#finds a "blank" space in the board, which is represented by a 0
def find_blank(board):
    for i in range(dim):
        for j in range(dim):
            if board[i][j] == 0:
                return (i, j)
    return None


#checks to see if the number being placed at the given position is valid given the rules of the game
# num - number being inserted, i.e. number whose validity is being tests
# pos - the position on the board ([i][j]) where the number is being inserted 
def is_valid(board, num, pos):

    #check #check if the num conflicts with the column
    for i in range(dim):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    #check if the num conflicts with the row
    for i in range(dim):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    #check if num conflicts with its 3x3 box neighbors
    #board can be thought of as a 3x3 grid of 3x3 boxes
    xBox = pos[1] // 3
    yBox = pos[0] // 3

    #nested for loops parse through all numbers in the 3x3
    for i in range(yBox*3, yBox*3 + 3):
        for j in range(xBox*3, xBox*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    #all 3 tests passsed, meaning this number fits in the given position
    return True


#solves the sudoku board using the previous functions
def solve(baord):
    blank = find_blank(board)

    #if a blank space is not found, the board is complete
    if not blank:
        return True
    else:
        row, column = blank

    #need to try inserting all possible numbers 1 thru 9
    for i in range (1, 10):
        if is_valid(board, i, (row, column)):
            board[row][column] = i
            if solve(board):
                return True
            
            #if the above recursive call of solve does not result in a solution, this insertion will get reset to 0, hence the "backtracking"
            board[row][column] = 0
    
    return False


#prints the results of the program
def print_solution(board):
    print_board(board)

    #solvable
    if solve(board):
        print("\nsolution:")
        print_board(board)

    #not solvable
    else:
        print("Board is unsolvable!")


#run the program
print_solution(board)