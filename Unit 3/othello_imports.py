#Anirudh Mantha
board = "...........................ox......xo..........................."
directions = [-11, -10, -9, -1, 1, 9, 10, 11]

def string_to_grid(board):
    retgrid = []
    for i in range(len(board)):
        if i % len(board)**0.5 == 0:
            row = board[i:i + len(board)**0.5 ]
            grid = [j for j in row]
            retgrid.append(grid)
    return retgrid

def grid_to_string(grid):
    return "".join(["".join([str(elem) for elem in sub]) for sub in grid])

def add_question_marks(board):
    #returnboard = "???????????........??........??........??........??........??........??........??........???????????"
    returnboard = "??????????"
    for i in range(8):
        returnboard = returnboard + "?"
        returnboard = returnboard + board[i*8:i*8+8]
        returnboard = returnboard + "?"
    return returnboard + "??????????"

def remove_question_mark(board):
    return board[11:19] + board[21:29] + board[31:39] + board[41:49] + board[51:59] + board[61:69] + board[71:79] + board[81:89]


def possible_moves(board, token):
    blank = "."
    size = 100
    possible_moves_list = []
    bigboard = add_question_marks(board)
    you = "xo"["ox".index(token)]
    for i in range(size):
        if bigboard[i] == blank:
            for j in directions:
                move = i + j
                while bigboard[move] == you:
                    if bigboard[move + j] == token: possible_moves_list.append(i)
                    move += j
    #GETS POSSIBLE MOVES INTO A LIST IN TERMS OF A 10X10

    retlist = []
    for i in possible_moves_list:
        new = 8*(i//10-1)+(i%10-1)
        #getting the index on an 8x8 board
        retlist.append(new)

    return list(set(retlist))


def make_move(board, token, index):

    you = "xo"["ox".index(token)]
    size = 100
    blank = "."
    bigboard = add_question_marks(board)
    new_index = 10*(index//8+1)+(index%8+1)
    #bigboard = bigboard[:new_index] + token + bigboard[new_index + 1:]
    #the actual location

    if bigboard[new_index] == ".":
        #only move when blank

        for i in directions:
            move = new_index + i
            while bigboard[move] == you:
                # changing everything in the middle
                if bigboard[move + i] == token:
                    internalswap = move
                    while bigboard[internalswap] == you:
                        #actually swapping the values between
                        bigboard = bigboard[:internalswap] + token + bigboard[internalswap + 1:]
                        internalswap -= i
                        # everything elligible between

                move += i

    #add the actual value
    bigboard = bigboard[:new_index] + token + bigboard[new_index + 1:]

    #remove the 10x10 to an 8x8 at the end
    return remove_question_mark(bigboard)






