from collections import deque
import sys

f1 = sys.argv[1]
with open(f1) as f:
    line_list = [line.strip() for line in f]

def print_puzzle(strindex):
    s1 = line_list[strindex]
    row, col = int(s1[0]), int(s1[0])
    s1 = deque(s1[2::])
    m1 = [[s1.popleft() for x in range(row)] for y in range(col)]

    return m1

def find_goal(strindex):
    s1 = (line_list[strindex])[2::].replace(".", "")
    return "".join((sorted(s1))) + "."


def matrixtoline(matrix):
    print(matrix)

def get_children(strindex):
    matrix = print_puzzle(strindex)
    matrix2 = print_puzzle(strindex)
    matrix3 = print_puzzle(strindex)
    matrix4 = print_puzzle(strindex)
    print(matrix)
    empty = '.'
    s1 = line_list[strindex]
    row, col = int(s1[0]), int(s1[0])

    output = []

    emptyr = -1
    emptyc = -1

    breakoutloop = False
    for i in range(row):
        for j in range(col):
            #print(type(matrix[i][j]))
            if matrix[i][j] == empty:
                emptyr = i
                emptyc = j
                breakoutloop = True
                break
        if breakoutloop:
            break

    #print(emptyr, emptyc)

    if emptyr + 1 <= row-1:
        #print("i can go down")
        mmodD = matrix
        mmodD[emptyr][emptyc] = mmodD[emptyr + 1][emptyc]
        mmodD[emptyr+1][emptyc] = empty
        strout = ""
        for i in range(row):
            for j in range(col):
                strout += mmodD[i][j]
        output.append(strout)
        output.append("  ")

    if emptyr - 1 >= 0:
        #print("i can go up")
        mmodU = matrix2
        mmodU[emptyr][emptyc] = mmodU[emptyr - 1][emptyc]
        mmodU[emptyr-1][emptyc] = empty
        strout = ""
        for i in range(row):
            for j in range(col):
                strout += mmodU[i][j]
        output.append(strout)
        output.append("  ")


    if emptyc + 1 <= col-1:
         #print("i can go right")
         mmodR = matrix3
         mmodR[emptyr][emptyc] = mmodR[emptyr][emptyc+1]
         mmodR[emptyr][emptyc+1] = empty
         strout = ""
         for i in range(row):
             for j in range(col):
                 strout += mmodR[i][j]
         output.append(strout)
         output.append("  ")

    if emptyc - 1 >= 0:
        #print("i can go left")
        mmodL = matrix4
        mmodL[emptyr][emptyc] = mmodL[emptyr][emptyc-1]
        mmodL[emptyr][emptyc - 1] = empty
        strout = ""
        for i in range(row):
            for j in range(col):
                strout += mmodL[i][j]
        output.append(strout)
        output.append("  ")
    #print(matrix)
    return output

# print(get_children(1))
# input()


for i in range(len(line_list)):
    print("Line " + str(i) + " start state")
    m1 = print_puzzle(i)
    for j in m1:
        print(j)
    print("\n")
    print("Line " + str(i) + " goal state: " + find_goal(i))
    print("\n")
    print("Line " + str(i) + " children: " + "".join(get_children(i)))
    print("\n")






