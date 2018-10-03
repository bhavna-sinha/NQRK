import sys

# Count # of pieces in given row
def count_on_row(board, row):
    return sum( board[row] )

# Count # of pieces in given column
def count_on_col(board, col):
    return sum( [ row[col] for row in board ] )

# Count total # of pieces on board
def count_pieces(board):
    return sum([ sum(row) for row in board ] )

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    if problem == "nqueen":
        return "\n".join([ " ".join([ "X" if (r, c) in unav else "Q" if col else "_" for c,col in enumerate(row) ]) for r, row in enumerate(board)])
    elif problem == "nrook":
        return "\n".join([ " ".join([ "X" if (r, c) in unav else "R" if col else "_" for c,col in enumerate(row) ]) for r, row in enumerate(board)])
    elif problem == "nknight":
        return "\n".join([" ".join(["X" if (r, c) in unav else "K" if col else "_" for c, col in enumerate(row)]) for r, row in enumerate(board)])

# Add a piece to the board at the given position, and return a new board (doesn't change original)
def add_piece(board, row, col):
    #check for the row and coloumn if there is any queen previously present or not
    return board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:]
# Get list of successors of given board state
def successors(board):
    return [ add_piece(board, r, c) for r in range(0, N) for c in range(0,N) ]

def diagonal(board, r,c):
    row = r
    col = c
    while(row < N and col < N):
        if board[row][col]:
            return True
        row = row + 1
        col = col + 1

    row = r
    col = c
    while(row >= 0 and col >= 0):
        if board[row][col]:
            return True
        row = row - 1
        col = col - 1

    row = r
    col = c
    while(row >= 0 and col < N):
        if board[row][col]:
            return True
        row = row - 1
        col = col + 1

    row = r
    col = c
    while(row < N and col >= 0):
        if board[row][col]:
            return True
        row = row + 1
        col = col - 1

    return False

def check_knight(board, r, c):
    rows = [r + 2, r - 2]
    rows = [row for row in rows if row in range(0, N)]
    cols = [c + 1, c - 1]
    cols = [col for col in cols if col in range(0, N)]
    for row in rows:
        for col in cols:
            if board[row][col]:
                return True

    rows = [r + 1, r - 1]
    rows = [row for row in rows if row in range(0, N)]
    cols = [c + 2, c - 2]
    cols = [col for col in cols if col in range(0, N)]
    for row in rows:
        for col in cols:
            if board[row][col]:
                return True

    return False

def successors3(board):
    suc_states = []
    total = count_pieces(board)
    if(total < N):
        for r in range(0, N):
            if count_on_row(board, r):
                continue
            for c in range(0, N):
                if count_on_col(board, c):
                    continue
                if (r,c) in unav:
                    continue
                if problem == "nrook":
                    suc_states.append(add_piece(board, r, c))
                elif problem == "nqueen":
                    if diagonal(board, r,c):
                        continue
                    suc_states.append(add_piece(board, r, c))
                elif problem == "nknight":
                    if check_knight(board, r, c):
                        continue
                    else:
                        suc_states.append(add_piece(board, r, c))
    return suc_states


# check if board is a goal state
def is_goal(board):
    return count_pieces(board) == N and \
        all( [ count_on_row(board, r) <= 1 for r in range(0, N) ] ) and \
        all( [ count_on_col(board, c) <= 1 for c in range(0, N) ] )

# Solve n-rooks!
def solve(initial_board):
    fringe = [initial_board]
    #print(fringe)
    while len(fringe) > 0:
        #print(len(fringe))
        for s in successors3( fringe.pop() ):
            # print(printable_board(s))
            # print("-------------")
            if is_goal(s):
                return(s)
            fringe.append(s)
    return False



# This is N, the size of the board. It is passed through command line arguments.
unav = []
problem = str(sys.argv[1])
N = int(sys.argv[2])
pos_unavl = int(sys.argv[3])
print(sys.argv)
for i in range(4, len(sys.argv), 2):
    row = int(sys.argv[i]) - 1
    col = int(sys.argv[i+1]) - 1
    unav.append((row, col))




# The board is stored as a list-of-lists. Each inner list is a row of the board.
# A zero in a given square indicates no piece, and a 1 indicates a piece.
initial_board = [[0]*N]*N
solution = solve(initial_board)
#print ("Starting from initial board:\n" + printable_board(initial_board) + "\n\nLooking for solution...\n")
#solution = solve(initial_board)
print (printable_board(solution) if solution else "Sorry, no solution found. :(")