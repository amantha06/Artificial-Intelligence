import sys
import time
import random

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

    return set(retlist)


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

def find_next_move(board, token, depth):
    potential_scores = {}
    if token == "x":
        for i in possible_moves(board, token):
            mademove = make_move(board, token, i)
            potential_scores[i] = min_step(mademove, "o", depth-1)
        # bestval = max(potential_scores.values())
        # bestkey = [k for k, v in potential_scores.items() if v == bestval]

        # bestval = 0
        # allkeys = [i for i in potential_scores.keys()]
        # bestkey = random.choice(allkeys)
        # for key, value in potential_scores.items():
        #     if value > bestval:
        #         bestval = value
        #         bestkey = key

        bestval = max(potential_scores.values())
        bestkey = [k for k, v in potential_scores.items() if v == bestval]


    else:
        for i in possible_moves(board, token):
            mademove = make_move(board, token, i)
            potential_scores[i] = max_step(mademove, "x", depth-1)
        # bestval = min(potential_scores.values())
        # bestkey = [k for k, v in potential_scores.items() if v == bestval]
        # bestval = 0
        # allkeys = [i for i in potential_scores.keys()]
        # bestkey = random.choice(allkeys)
        # for key, value in potential_scores.items():
        #     if value < bestval:
        #         bestval = value
        #         bestkey = key
        bestval = min(potential_scores.values())
        bestkey = [k for k, v in potential_scores.items() if v == bestval]

    return int(bestkey[0])


def min_step(board, player, depth):
    opponent = "xo"["ox".index(player)]
    if depth == 0 or ((len(possible_moves(board, "x")) == 0 and len(possible_moves(board, "o")) == 0)):
        return score(board)

    if len(possible_moves(board, player)) == 0:
        return max_step(board, opponent, depth-1)

    results = []
    for i in possible_moves(board, player):
        results.append(max_step(make_move(board, player, i), opponent, depth-1))
    return min(results)


def max_step(board, player, depth):
    opponent = "xo"["ox".index(player)]
    if depth == 0 or (len(possible_moves(board, "x")) == 0 and len(possible_moves(board, "o")) == 0):
        return score(board)

    if len(possible_moves(board, player)) == 0:
        return min_step(board, opponent, depth-1)
    results = []
    for i in possible_moves(board, player):
        results.append(min_step(make_move(board, player, i), opponent, depth-1))
    return max(results)

def score(board):
    retscoreval = 0
    corners = [0, 7, 63, 56]
    next_corners = [1, 6, 8, 9, 14, 15, 48, 49, 54, 55, 57, 62]
    edges = [2, 3, 4, 5, 16, 24, 32, 40, 22, 30, 38, 44, 58, 59, 60, 61]
    if board.count(".") == 0:
        return int((board.count("x") - board.count("o"))*10000000000000000000000000)


    possible_x_moves = possible_moves(board, "x")
    possible_o_moves = possible_moves(board, "o")

    # current_place = {}
    #
    # for i in range(len(board)):
    #     if board[i] == "x":
    #         current_place[i] = "x"
    #     elif board[i] == "o":
    #         current_place[i] = "o"


    if len(possible_x_moves) > len(possible_o_moves):
        retscoreval += len(possible_x_moves)-len(possible_o_moves)*1000
    else:
        retscoreval -= len(possible_x_moves)-len(possible_o_moves)*1000

    for i in corners:
        if board[i] == "x":
            retscoreval += 10000000
        elif board[i] == "o":
            retscoreval -= 10000000

    # for i, v in current_place.items():
    #     if i in corners and v == "x":
    #         retscoreval += 1000000
    #     if i in corners and v == "o":
    #         retscoreval -= 1000000


    for i in next_corners:
        if i == 1 or i == 8 or i == 9:
            if board[i] == "x" and board[0] == ".":
                retscoreval -= 500000
            elif board[i] == "x" and board[0] == "x":
                retscoreval += 500000
            elif board[i] == "o" and board[0] == ".":
                retscoreval += 500000
            elif board[i] == "o" and board[0] == "o":
                retscoreval -= 500000
        if i == 6 or i == 14 or i == 15:
            if board[i] == "x" and board[7] == ".":
                retscoreval -= 500000
            elif board[i] == "x" and board[7] == "x":
                retscoreval += 500000
            elif board[i] == "o" and board[7] == ".":
                retscoreval += 500000
            elif board[i] == "o" and board[7] == "o":
                retscoreval -= 500000
        if i == 48 or i == 49 or i == 57:
            if board[i] == "x" and board[56] == ".":
                retscoreval -= 500000
            elif board[i] == "x" and board[56] == "x":
                retscoreval += 500000
            elif board[i] == "o" and board[56] == ".":
                retscoreval += 500000
            elif board[i] == "o" and board[56] == "o":
                retscoreval -= 500000


    for i in edges:
        if board[i] == "x":
            retscoreval += 45000
        if board[i] == "o":
            retscoreval -= 45000

    if board.count(".") <= 20:
        #greedy
        None
    return retscoreval + random.choice([1, 2, 3, 4, 5, 6, 7])


class Strategy():

   logging = True  # Optional

   def best_strategy(self, board, player, best_move, still_running):

       depth = 1

       for count in range(board.count(".")):  # No need to look more spaces into the future than exist at all

           best_move.value = find_next_move(board, player, depth)

           depth += 1