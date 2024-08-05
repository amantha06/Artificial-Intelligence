import heapq
from collections import deque
from time import perf_counter
from heapq import heappush, heappop, heapify

line_list = ["3 @@@@@.@.. 8"]
cube = tuple([[0, 0], [0, 0], [0, 0]])

def make_board_cube(strboard, startspot):
    size = int(len(strboard)**0.5)
    start_index = 0
    strboard = strboard[:startspot] + "*" + strboard[startspot+1:]
    for i in range(size):
        print(strboard[start_index: start_index+size])
        start_index += size

    return strboard
    #front, back, up down, right left

def get_children():
    return 0

make_board_cube(line_list[0][2:-1:], int(line_list[0][-1]))

