import heapq
from collections import deque
from time import perf_counter
from heapq import heappush, heappop, heapify


import sys

f1 = sys.argv[1]
#line_list = ["3 ABCDEFG.H", "3 87436.152", "3 .25187643", "3 863.54217"]

with open(f1) as f:
     line_list = [line.strip() for line in f]

def print_puzzle(strindex):
    # s1 = line_list[strindex]
    s1 = strindex
    row, col = int(len(strindex)**0.5), int(len(strindex)**0.5)
    #row, col = int(s1[0]), int(s1[0])
    s1 = deque(s1)
    m1 = [[s1.popleft() for x in range(row)] for y in range(col)]

    return m1


def find_goal(strindex):
    # s1 = (line_list[strindex])[2::].replace(".", "")
    s1 = (strindex).replace(".", "")
    return "".join((sorted(s1))) + "."


def toline(strindex):
    # s1 = (line_list[strindex])[2::]
    s1 = (strindex)
    return "".join(s1)


def get_children(strindex):
    matrix = print_puzzle(strindex)
    matrix2 = print_puzzle(strindex)
    matrix3 = print_puzzle(strindex)
    matrix4 = print_puzzle(strindex)
    # print(matrix)
    empty = '.'

    row, col = int(len(strindex)**0.5), int(len(strindex)**0.5)

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
    if emptyr + 1 <= row - 1:
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
        mmodU = matrix2
        mmodU[emptyr][emptyc] = mmodU[emptyr - 1][emptyc]
        mmodU[emptyr - 1][emptyc] = empty
        strout = ""
        for i in range(row):
            for j in range(col):
                strout += mmodU[i][j]
        output.append(strout)

    if emptyc + 1 <= col - 1:
        mmodR = matrix3
        mmodR[emptyr][emptyc] = mmodR[emptyr][emptyc + 1]
        mmodR[emptyr][emptyc + 1] = empty
        strout = ""
        for i in range(row):
            for j in range(col):
                strout += mmodR[i][j]
        output.append(strout)

    if emptyc - 1 >= 0:
        mmodL = matrix4
        mmodL[emptyr][emptyc] = mmodL[emptyr][emptyc - 1]
        mmodL[emptyr][emptyc - 1] = empty
        strout = ""
        for i in range(row):
            for j in range(col):
                strout += mmodL[i][j]
        output.append(strout)
        output.append("  ")
    return output




def bfs(start):
    row = start[0]
    startstr = start[2::]

    fringe = deque()
    visited = set()

    fringe.append(tuple([startstr, 0]))
    visited.add(startstr)
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

def bibfs(start):
    row = start[0]
    startstr = start[2::]
    end = find_goal(startstr)

    fringe_for = deque()
    fringe_back = deque()
    visited_for = set()
    visited_back = set()

    fringe_for.append(tuple([startstr, 0]))
    visited_for.add(startstr)

    fringe_back.append(tuple([end, 0]))
    visited_back.add(end)

    while len(fringe_back) > 0 and len(fringe_for) > 0:
        vfor = fringe_for.popleft()
        if vfor[0] in visited_back:
            return vfor[1]
        storef = get_children(str(row) + " " + (vfor[0]))
        for i in storef:
            if i == "  ":
                storef.remove(i)

        for i in storef:
            if i not in visited_for:
                visited_for.add(i)
                fringe_for.append(tuple([i, vfor[1]+1]))

        vback = fringe_back.popleft()
        if vback[0] in visited_for:
            return vback[1]
        storeb = get_children(str(row) + " " + (vback[0]))
        for i in storeb:
            if i == "  ":
                storeb.remove(i)

        for i in storeb:
            if i not in visited_back:
                visited_back.add(i)
                fringe_back.append(tuple([i, vback[1]+1]))
    return None

def parity(strboard):
    #412836.75
    size = len(strboard)**0.5
    num_otopairs = 0
    check_oto = []
    newstr = strboard.replace(".", "")
    for i in newstr:
        check_oto.append(i)
        for j in check_oto:
            if i < j:
                num_otopairs += 1
    if size % 2 != 0:
        if num_otopairs % 2 != 0:
            return True
        return False

    if size % 2 == 0:
        blankrow = strboard.find(".")//size
        if blankrow % 2 == 0 and num_otopairs % 2 != 0:
            return False
        elif blankrow % 2 != 0 and num_otopairs % 2 == 0:
            return False
        else:
            return True

def taxicab(strboard):
    goal = find_goal(strboard)
    dist = 0
    size = len(strboard)**0.5
    for i, v in enumerate(strboard):
        if v != ".":
            #this is the main logic behind the taxicab
            #splitting distance into horizontal moves and vertical moves
            #horizontal means floor divide from the desired location and where you are to the size
            #vertical means to modulous the same values to get the vertical moves
            #this method can also be completed through using a matrix but that is messier
            horcomp = abs(goal.find(v) // size - i // size)
            vertcomp = abs(goal.find(v) % size - i % size)
            dist += (vertcomp + horcomp)
    return int(dist)



def astar(strboard):
    closed = set()
    f = taxicab(strboard)
    fringe = []
    heapq.heapify(fringe)
    heapq.heappush(fringe, (f, 0, strboard))
    while len(fringe) > 0:
        v = heapq.heappop(fringe)
        if find_goal(strboard) == v[2]:
            return v[1]
        if v[2] not in closed:
            closed.add(v[2])

            children = get_children(v[2])
            for i in children:
                if i == "  ":
                    children.remove(i)
            for i in children:
                if i not in closed:
                    tempdepth = v[1] + 1
                    temptaxi = tempdepth + taxicab(i)
                    #f(x) + g(x)
                    heapq.heappush(fringe, (temptaxi, tempdepth, i))
    return None




for i, v in enumerate(line_list):
    start = perf_counter()
    # print(bibfs(v))
    if not parity(v[2::]):
        print("line ", i, ": ", astar(v[2::]), " ", perf_counter()-start)
    else:
        print("line ", i, "no solution! ", perf_counter() - start)



# for i in range(len(line_list)):
#     start = perf_counter()
#     #print("BFS: Line ", (i), ": ", line_list[i], ", ", (bfs(line_list[i])), " moves found in ", (perf_counter() - start))
#     print("Bi BFS: Line ", (i), ": ", line_list[i], ", ", (bibfs(line_list[i])), " moves found in ", (perf_counter() - start))
#
#
#



