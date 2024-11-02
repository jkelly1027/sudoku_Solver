# Find a solution to a given board using back tracking algorithm.
# Can't have the same number twice in a row, column, or box.
# Much more efficient than a Naive approach.
# Back Tracking Algorithm:
# 1) Pick empty square.
# 2) Try numbers 1-9. Find one that works within the parameters of the game.
# 3) Move to the next empty square, repeat step 2.
# Repeat the process until we come to a square with no valid solution.
# Back track to the previous square and continue trying numbers from n + 1 where n is the last number we tried in that square.
# If no valid solution is found in this square after backtracking we back track again.
# This process is repeated until all squares are valid.

# Starting board
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# Print the board
def print_board(board):

    # Divide the board into 9 squares
    # Horizontal lines (Every 3 rows)
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("---------------")

        # Vertical Lines
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0: # Dont want a line on the far left (j != 0)
                print(" | ", end="") # end="" means dont go to next line

            # Print the rows of the board
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + "", end="")

# Finds empty square, returns its position.
def find_empty(board):

    # Loop through Board
    for i in range(len(board)):
        for j in range(len(board[0])):
            
            # Check if empty
            if board[i][j] == 0:
                return(i, j) # Tuple, row & col
            
    return None
            
# Check if the given board is valid (number = num inserted, position = where we are inserting(tuple i j))
def valid(board, number, position):

    # Check row (Loop through each col in row)
    for i in range(len(board[0])):
        # position[row][col]                   position[col]
        # Check the other squares in row, if num is equal to that square and that square isn't the square we just inserted into then not valid.
        if board[position[0]][i] == number and position[1] != i:
            return False

    # Check col (Loop through each row in col)
    for i in range(len(board)):
        # position[row][col]                   position[row]
        # Check the other squares in col, if num is equal to that square and that square isn't the square we just inserted into then not valid.
        if board[i][position[1]] == number and position[0] != i:
            return False

    # Check square (Need to determine which box were in)
    box_x = position[1] // 3
    box_y = position[0] // 3

    # Then loop through all 9 elements within a box. (n to n+3 for both x,y)
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            # Not valid if square were checking is equal to num and that square isn't the one we just added to.
            if board[i][j] == number and (i,j) != position:
                return False
            
    # If we pass all checks return True
    return True

# Back Tracking Algorithm (Recursive func)
def solve(board):

    # Call func to find empty square
    find = find_empty(board)

    # Base case: If find_empty returns false there are no empty square left.
    if not find:
        return True # Solution Found!
    # Else find_empty returns the row/col of next empty square
    else:
        row, col = find

    # Loop through possible values, attempt to put in solution
    for i in range(1,10):
        if valid(board, i, (row, col)):
            # If the number is valid plug it into the board at position row/col
            board[row][col] = i

            # Then we will recursively try to reach a solution by call solve() on our new/updated board
            # 1) Keeping going until we either reach a solution or we've tried all numbers 1-9 for a square
            if solve(board):
                return True

            # 3) Reset the last square to 0, continue to the next number to try in this square
            board[row][col] = 0

    # 2) If all numbers 1-9 are invalid solve returns false. We then backtrack, come out one level of recursion 
    return False

# Print the Starting board
print("\nStarting Board\n")
print_board(board)

# Solve the board
solve(board)

# Print the solved board
print("\nSolved Board\n")
print_board(board)