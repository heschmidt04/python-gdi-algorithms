"""
# Day 6 -- https://replit.com/@lizthedeveloper/GDI-Technical-Interview-Prep-Tic-Tac-Toe-and-Which-Light#main.py

## sudoku, connect 4, 

## Given a tic-tac-toe board as a two-dimensional array (aka list), 
## determine the winner! 
## There are 0s, representing an empty space, 
## 		1 representing the first player
## 	, and 2 representing the second player.

## Write a function like so: tic_tac_toe_win_check(board)
## Returns the winner 1 or 2 or shows a draw of 0 

# 2 dimensional array 
# 1 is winning in the examples below 
"""

tic_tac_toe_row = [
    [1, 1, 1],
    [0, 2, 0],
    [2, 0, 2]
]

tic_tac_toe_row_too = [
    [0, 2, 1],
    [1, 1, 1],
    [2, 0, 2]
]

tic_tac_toe_column = [
    #  0 1 2 
    [2, 1, 0],
    [0, 1, 0],
    [0, 1, 2]
]

tic_tac_toe_column_too = [
    #  0 1 2 
    [2, 1, 1],
    [0, 2, 1],
    [0, 1, 1]
]

tic_tac_toe_diag = [
    [2, 0, 1],
    [0, 1, 2],
    [1, 0, 2]
]


def check_row_win(row):
    """
        If the value returned is 0 then no winners
        If the value is a 1 or a 2 then they won
        NOTE: The value of 3 zeroes is not possible and also not accounted for 
    """
    first_num = row[0]
    for num in row:
        if num != first_num:
            return 0
    return first_num


def check_column_win(column, board):
    """
    For the first position on the board 
                         R  C
      tic_tac_toe_column[0][0]
      tic_tac_toe_column[1][0]
      tic_tac_toe_column[2][0]

    For the middle position on the board 
                         R  C
      tic_tac_toe_column[0][1]
      tic_tac_toe_column[1][1]
      tic_tac_toe_column[2][1]

    For the end position on the board 
                         R C
      tic_tac_toe_column[0][2]
      tic_tac_toe_column[1][2]
      tic_tac_toe_column[2][2]
    """
    # start at row 0 
    first_num = board[0][column]
    print(f"This is first num: {first_num}")
    for row in range(len(board)):
        print(f"This is the row: {row}")
        # check each row at the same column number
        if board[row][column] != first_num:
            print(f"This is the {board[row][column]}")
            return 0
    return first_num


# From screen shot 
def check_column_win(column, board):
    first_num = board[0][column]
    for row in range(len(board)):
        ## check each row at the same column number
        if (board[row][column]) != first_num:
            return 0
    return first_num


def tic_tac_toe_win_check(board, column=None):
    """
        How do we determine a winner? 
        Check each row 
            Is the number in the 1st, 2nd, and 3rd place then they won - return that number 
        Check the column 
            Start at column 0 row 0 and check each col 0 row1  
                and col 0 row3 and so on for other cols - return the number 
        Check the diagonal 
            Start at col 0, row 0  
                     col 1, row 1 
                     col 3, row 2 
    """
    for row in board:
        #	check_row_win(row)
        win = check_row_win(row)
        if win != 0:
            return (f"This row was the winner! {win}")

        # What is happening is that it does not increment through the rest of the columns - it does col 0 and then ends 
    # Adding a column counter to see if it increments 
    for column in range(len(board)):
        win = check_column_win(column, board)
        print(
            f"This is what win is set to from check_column_win: {win} for the column and board position of {column}, in {board}")
        if win != 0:  # The problem was with check column win -- was set to always return a 0 and so it would never evaluate 
            return (f"This column was the winner! {win}")
        elif win == None:
            return (f"We recieved back a None Type")
        else:
            return (f"Argh! something else happened")
    column += 1


## Diagonal -- may look ugly but it is accurate 
# 		left diagonal 
center = board[1][1]
if center == board[0][2] and center == board[2][0]:
    print(f"This is the diagonal left {center}")
# 		right diagonal 
if center == board[0][0] and center == board[2][2]:
    print(f"This is the diagonal right {center}")

print(tic_tac_toe_win_check(tic_tac_toe_row))
print(tic_tac_toe_win_check(tic_tac_toe_column))  # returns a None type 
print(tic_tac_toe_win_check(tic_tac_toe_diag))