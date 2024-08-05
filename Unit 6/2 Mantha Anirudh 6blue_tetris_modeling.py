import sys
import time
import os

height = 20
width = 10

def update_state(board, piece, c, top):
    if c + piece.index("X") > width: return "GAME OVER"
    ind = top * width + c
    for i in piece:
        if top < 0: return "GAME OVER"
        if i == "X":
            top = top - 1
            ind = top * width + c
        elif board[ind] == "#" and i == "#": return "GAME OVER"
        else:
            if i == "#": board = board[:ind] + "#" + board[ind + 1:]
        ind = ind + 1
    return board

def insert(board, piece, c):
    final_state = "GAME OVER"
    for i in range(piece.count("X") - 1, height):
        state = update_state(board, piece, c, i)
        if state == "GAME OVER": return final_state
        else: final_state = state
    return final_state

def clear_level(board):
    temp = 0
    for i in range(height):
        if board[i*width: (i*width) + 10] == "#" * width:
            board = ("" * width) + board[: i*width] +board[i*width + width:]
            temp = temp + 1
    return board, temp

initial_time = time.perf_counter()
board = "".join(sys.argv[1])
output = []
pieces = {
    "I": ["####", "####"],
    "O": ["####"],
    "T": ["### # ", "# ### ", " # ###", " ### #"],
    "S": ["##  ##", " #### "],
    "Z": [" #### ", "# ## #"],
    "J": ["####  ", "# # ##", "  ####", "## # #"],
    "L": ["###  #", "### # ", "#  ###", " # ###"],
}
if os.path.isfile("tetrisout.txt"):
    os.remove("tetrisout.txt")
    #print("FILE MADEEE")
outfile = open("tetrisout.txt", "x")
    #print("AJLKDFAJLKF")

for i in pieces:
    for j in pieces[i]:
        for k in range(10-j.index("X")):
            an_output = insert(board, j, k)
            an_output, _num_levels_cleared = clear_level(an_output)
            #print(an_output)
            output.append(an_output)
            outfile.write(an_output + "\n")
outfile.close()
print(time.perf_counter() - initial_time)






