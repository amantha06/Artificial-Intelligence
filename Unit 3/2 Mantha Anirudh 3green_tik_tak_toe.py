import heapq
from collections import deque
from time import perf_counter
from heapq import heappush, heappop, heapify
import sys

def display(board):
    print("Current board: ")
    print(board[0:3], "  -  0 1 2")
    print(board[3:6], "  -  3 4 5")
    print(board[6:9], "  -  6 7 8")

def string_to_grid(board):
    retgrid = []
    for i in range(9):
        if i % 3 == 0:
            row = board[i:i + 3]
            grid = [j for j in row]
            retgrid.append(grid)
    return retgrid
#make into a grid
#0 is tie
#1 is X
#-1 is O

def grid_to_string(grid):
    return "".join(["".join([str(elem) for elem in sub]) for sub in grid])

def check(board):
    for i in range(0, 3):
        if board[0][i] == board[1][i] == board[2][i] == "X" \
                or board[i][0] == board[i][1] == board[i][2] == "X" \
                or board[0][0] == board[1][1] == board[2][2] == "X" \
                or board[2][0] == board[1][1] == board[0][2] == "X":
            return 1


        elif board[0][i] == board[1][i] == board[2][i] == "O" != " " \
                or board[i][0] == board[i][1] == board[i][2] == "O" != " " \
                or board[0][0] == board[1][1] == board[2][2] == "O" != " " \
                or board[2][0] == board[1][1] == board[0][2] == "O" != " ":
            return -1

    if "." not in grid_to_string(board): return 0

    return None

def possible_next_boards(board, player):
    count = [i for i in range(len(board)) if board[i] == "."]
    retlist = {}
    for i in count:
        temp = board
        temp = temp[:i] + player + temp[i+1:]
        retlist[i] = temp
    #retlist = [board[i].replace(board[i], player) for i in count]

    return retlist

#change result into a dictionary
def max_step(board):
    if check(string_to_grid(board)) != None:
        return check(string_to_grid(board))
    results = []
    for i in possible_next_boards(board, "X").values():
        results.append(min_step(i))

    return max(results)
def min_step(board):
    if check(string_to_grid(board)) != None:
            return check(string_to_grid(board))
    results = []
    for i in possible_next_boards(board, "O").values():
        results.append(max_step(i))
    return min(results)


# 255168 different games
# 958 final boards
# X in 5: 120
# X in 7: 444
# X in 9: 62
# O in 6: 148
# O in 8: 168
# Draw: 16
def countXO(board):
    xcount = 0
    ocount = 0
    count = 0
    for i in board:
        if i == "X": xcount += 1
        if i == "O": ocount += 1
        if i == ".": count+=1
    return xcount, ocount


def play(board, player, myturn):
    win = None
    loss = None
    if player == "O":
        win = -1
        loss = 1
    else:
        win = 1
        loss = -1

    updateboard = board
    while check(string_to_grid(board)) == None:
        updateboard = board
        if myturn:
            if player == "X":
                me = "O"
            else:
                me = "X"
            posmoveslist = [i for i in range(len(board)) if board[i] == "."]
            posmoves = str(posmoveslist[0])
            for i in posmoveslist[1:]:
                posmoves = posmoves + ", " + str(i)
            display(board)
            print("You can move to any of these spaces: " + posmoves)
            move = int(input("Your move? "))
            board = board[:move] + me + board[move+1:]
            display(board)

            if check(string_to_grid(board)) != None:
                return check(string_to_grid(board))

            if myturn == True:
                myturn = False
            elif myturn == False:
                myturn = True
            # if player == "X":
            #     antiplayer = "O"
            #     posmovesdict = possible_next_boards(board, antiplayer)
            #     for k, v in posmovesdict.items():
            #         print("Moving at ", k, "results in ", max_step(v))
            #         # input()
            #
            # if player == "O":
            #     antiplayer = "X"
            #     posmovesdict = possible_next_boards(board, antiplayer)
            #     for k, v in posmovesdict.items():
            #         print("Moving at ", k, "results in ", min_step(v))

        else:
            if player == "X":
                antiplayer = "O"
                posmovesdict = possible_next_boards(board, player)
                maxkey, maxval = None, -2
                for k, v in posmovesdict.items():
                    temp = min_step(v)
                    rettemp = ""
                    if temp == win:
                        rettemp = "win"
                    elif temp == loss:
                        rettemp = "loss"
                    else:
                        rettemp = "tie"
                    print("Moving at ", k, "results in a ", rettemp)
                    if temp > maxval:
                        maxkey, maxval = k, temp
                print("I am moving at ", maxkey)

                board = board[:maxkey] + player + board[maxkey+1:]
                display(board)
                    # input()

            if player == "O":
                antiplayer = "X"
                posmovesdict = possible_next_boards(board, player)
                minkey, minval = None, 2
                for k, v in posmovesdict.items():
                    temp = max_step(v)
                    rettemp = ""
                    if temp == win:
                        rettemp = "win"
                    elif temp == loss:
                        rettemp = "loss"
                    else:
                        rettemp = "tie"

                    print("Moving at ", k, "results in a ", rettemp)
                    if temp < minval:
                        minkey, minval = k, temp

                print("I am moving at ", minkey)
                board = board[:minkey] + player + board[minkey+1:]
                display(board)


            if check(string_to_grid(board)) != None:
                return check(string_to_grid(board))

            if myturn == True:
                myturn = False
            elif myturn == False:
                myturn = True
        updateboard = board
    return check(string_to_grid(board))

board = sys.argv[1]
while len(board) != 9:
    board = input("Please try again: please enter a board: 9 characters ONLY X/O/. : ")

myturn = None

if(board == "........."):
    p1 = input("Should I be X or O - please respond with capital letters: ")
    if p1 == "X": myturn = False
    else: myturn = True

else:
    myturn = False
    x, o = countXO(board)
    if x == o: p1 = "X"
    else: p1 = "O"

winner = play(board, p1, myturn)

if winner == 0:
    print("We tied!")
if p1 == "X" and winner == 1 or p1 == "O" and winner == -1:
    print("I win")
if p1 == "X" and winner == -1 or p1 == "O" and winner == 1:
    print("You win")







