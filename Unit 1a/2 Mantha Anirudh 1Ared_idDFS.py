from collections import deque
from time import perf_counter

import sys

f1 = sys.argv[1]
with open(f1) as f:
   line_list = ["4 " + line.strip() for line in f]


#line_list = ["4 ABCDEFGHIJKLMNO."]

def print_puzzle(strindex):
    # s1 = line_list[strindex]
    s1 = strindex
    row, col = int(s1[0]), int(s1[0])
    s1 = deque(s1[2::])
    m1 = [[s1.popleft() for x in range(row)] for y in range(col)]

    return m1


def find_goal(strindex):
    # s1 = (line_list[strindex])[2::].replace(".", "")
    s1 = (strindex).replace(".", "")
    return "".join((sorted(s1))) + "."


def toline(strindex):
    # s1 = (line_list[strindex])[2::]
    s1 = (strindex)[2::]
    return "".join(s1)


def get_children(strindex):
    matrix = print_puzzle(strindex)
    matrix2 = print_puzzle(strindex)
    matrix3 = print_puzzle(strindex)
    matrix4 = print_puzzle(strindex)
    # print(matrix)
    empty = '.'

    row, col = int(strindex[0]), int(strindex[0])

    output = []

    emptyr = -1
    emptyc = -1

    breakoutloop = False
    for i in range(row):
        for j in range(col):
            # print(type(matrix[i][j]))
            if matrix[i][j] == empty:
                emptyr = i
                emptyc = j
                breakoutloop = True
                break
        if breakoutloop:
            break

    # print(emptyr, emptyc)

    if emptyr + 1 <= row - 1:
        # print("i can go down")
        mmodD = matrix
        mmodD[emptyr][emptyc] = mmodD[emptyr + 1][emptyc]
        mmodD[emptyr + 1][emptyc] = empty
        strout = ""
        for i in range(row):
            for j in range(col):
                strout += mmodD[i][j]
        output.append(strout)
        output.append("  ")

    if emptyr - 1 >= 0:
        # print("i can go up")
        mmodU = matrix2
        mmodU[emptyr][emptyc] = mmodU[emptyr - 1][emptyc]
        mmodU[emptyr - 1][emptyc] = empty
        strout = ""
        for i in range(row):
            for j in range(col):
                strout += mmodU[i][j]
        output.append(strout)

    if emptyc + 1 <= col - 1:
        # print("i can go right")
        mmodR = matrix3
        mmodR[emptyr][emptyc] = mmodR[emptyr][emptyc + 1]
        mmodR[emptyr][emptyc + 1] = empty
        strout = ""
        for i in range(row):
            for j in range(col):
                strout += mmodR[i][j]
        output.append(strout)

    if emptyc - 1 >= 0:
        # print("i can go left")
        mmodL = matrix4
        mmodL[emptyr][emptyc] = mmodL[emptyr][emptyc - 1]
        mmodL[emptyr][emptyc - 1] = empty
        strout = ""
        for i in range(row):
            for j in range(col):
                strout += mmodL[i][j]
        output.append(strout)
        output.append("  ")
    # print(matrix)
    return output

def kdfs(start, k):
    row = int(len(start)**0.5)
    visited = set()
    fringe = deque()
    fringe.append(tuple([start, 0, {start}]))

    visited.add(start)

    while len(fringe) > 0:
         v, step, visited = fringe.pop()
         if find_goal(v) == v:
             return step
         if step < k:
             store = get_children(str(row) + " " + (v))

             for i in store:
                 if i == "  ":
                     store.remove(i)

             for i in store:
                 if i not in visited:
                     c_step = step + 1
                     newancestor = visited.copy()
                     newancestor.add(i)
                     fringe.append(tuple([i, c_step, newancestor]))
    return None

# def kdfs(start, k):
#     row = int(len(start)**0.5)
#     fringe = deque()
#     ancestors = set()
#     ancestors.add(start)
#     fringe.append(start, 0)
#
#     while len(fringe) > 0:
#         v, depth = fringe.pop()
#         if find_goal(v) == v:
#             return v
#         if depth < k:
#             store = get_children(str(row) + " " + (v))
#
#             for i in store:
#                 if i == "  ":
#                     store.remove(i)
#
#             for i in store:
#                 if i not in ancestors:
#                     temp = i, depth + 1

def iddfs(start):
    startstr = start[2::]
    max = 0
    finalvar = None
    while finalvar is None:
        finalvar = kdfs(startstr, max)
        max = max + 1
    return finalvar

def bfs(start):
    row = start[0]
    startstr = start[2::]

    fringe = deque()
    visited = set()

    fringe.append(tuple([startstr, 0]))
    visited.add(startstr)
    # dvisited.append()
    while len(fringe) > 0:
        v = fringe.popleft()

        goal = find_goal(startstr)
        if v[0] == goal:
            return v[1]

        store = get_children(str(row) + " " + (v[0]))
        for i in store:
            if i == "  ":
                store.remove(i)

        for i in store:
            if i not in visited:
                visited.add(i)
                fringe.append(tuple([i, v[1] + 1]))
                if i == goal:
                    return fringe.pop()

    return None


for i in range(len(line_list)):
    start = perf_counter()
    print(line_list[i])
    print("Line ", (i), ": ", line_list[i], ", ", (bfs(line_list[i])), " moves found in ", (perf_counter() - start))
    print("Line ", (i), ": ", line_list[i], ", ", (iddfs(line_list[i])), " moves found in ", (perf_counter() - start))




