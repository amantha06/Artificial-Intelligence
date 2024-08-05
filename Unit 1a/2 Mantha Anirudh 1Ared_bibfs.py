from collections import deque
from time import perf_counter

import sys

f1 = sys.argv[1]

with open(f1) as f:
    line_list = [line.strip() for line in f]


#line_list = ["3 .25187643"]

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
                    return fringe.pop()[1]

    return None

#         2 A.CB, ABC.
def bibfs(start):
    row = start[0]
    startstr = start[2::]
    end = find_goal(startstr)
    #TRIED FIXING WITH USING DICT INSTEAD OF SET, BUT TIMING IS SAME.. I AM CONVINCED THAT THE TIMING IS NOT A PROBLEM
    fringe_for = deque()
    fringe_back = deque()
    visited_for = dict()
    visited_back = dict()
    #using dict made no differnece in time, I could switch back to set again, but I guess it is no harm

    fringe_for.append(tuple([startstr, 0]))
    visited_for[startstr] = [startstr]

    fringe_back.append(tuple([end, 0]))
    visited_back[end] = [end]

    while len(fringe_back) > 0 and len(fringe_for) > 0:
        if len(fringe_for) > 0:
            vfor = fringe_for.popleft()
            if vfor[0] in visited_back.keys():
                return len(visited_for[vfor[0]]) + len(visited_back[vfor[0]]) - 2 #-2 for the overlaps
                                                                                  # 1 error from last time is that I just returned the vfor[0] value so it gave 1/2 of the right answer
            storef = get_children(str(row) + " " + (vfor[0]))


            for i in storef:
                if i == "  ":
                    storef.remove(i)

            for i in storef:
                if i not in visited_for.keys():
                    visited_for[i] = list(visited_for[vfor[0]])
                    visited_for[i].append(i)
                    fringe_for.append(tuple([i, vfor[1] + 1]))

        if len(fringe_back) > 0:
            vback = fringe_back.popleft()
            if vback[0] in visited_for.keys():
                return len(visited_back[vback[0]]) + len(visited_for[vback[0]]) - 2
            storeb = get_children(str(row) + " " + (vback[0]))


            for i in storeb:
                if i == "  ":
                    storeb.remove(i)

            for i in storeb:
                if i not in visited_back.keys():
                    visited_back[i] = list(visited_back[vback[0]])
                    visited_back[i].append(i)
                    fringe_back.append(tuple([i, vback[1] + 1]))

    return None


for i in range(len(line_list)):
    start = perf_counter()
    bfsval = (bfs(line_list[i]))
    print("BFS: Line ", (i), ": ", line_list[i], ", ", bfsval, " moves found in ", (perf_counter() - start))

    start = perf_counter()
    print("Bi BFS: Line ", (i), ": ", line_list[i], ", ", int((bibfs(line_list[i]))), " moves found in ", (perf_counter() - start))


# print(bfs("3 12345678."))
# print(bfs("3 8672543.1"))


# while fringe is not empty do:
#     v = fringe.pop()
# if GoalTest(v) then:
#     return v
# for every child c of v do:
#     if c not in visited then:
#         fringe.add(c)
# visited.add(c)
# return None