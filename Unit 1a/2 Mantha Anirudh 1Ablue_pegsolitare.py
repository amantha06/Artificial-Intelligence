from collections import deque
from time import perf_counter
import sys

startstate = "011111111111111"
goalstate = "100000000000000"
#hardcoded moves in a dictionary
#tuples used because python is good at unpacking
#each index has the possible moves as children
possiblemoves = {0: tuple([[1,3], [2,5]]), 1: tuple([[3,6], [4,8]]), 2: tuple([[4,7], [5,9]]), 3: tuple([[1,0], [6,10], [7,12], [4,5]]), 4: tuple([[7,11], [8,13]]), 5: tuple([[2,0], [8,12], [9,14], [4,3]]), 6: tuple([[3,1], [7,8]]), 7: tuple([[4,2], [8,9]]), 8: tuple([[4,1], [7,6]]), 9: tuple([[5,2], [8,7]]), 10: tuple([[6,3], [11,12]]), 11: tuple([[7,4], [12,13]]), 12: tuple([[7,3], [8,5], [11,10], [13,14]]), 13: tuple([[8,4], [12,11]]), 14: tuple([[9,5], [13,12]])}

def format(s):
    print("       ", s[0])
    print("     ", s[1], " ", s[2])
    print("   ", s[3], " ", s[4], " ", s[5])
    print(" ", s[6], " ", s[7], " ", s[8], " ", s[9])
    print(s[10], " ", s[11], " ", s[12], " ", s[13], " ", s[14])

def get_children(parent):
    output = []
    for i, v in enumerate(parent):
        if v == "0":
            store = possiblemoves[i]
            temp = i
            #find the values that have no peg, and get their possible moves
            #iterate through those possible moves

            for j in range(len(store)):
                #now see if the possible moves are actually possible or not
                if parent[store[j][0]] == "1" and parent[store[j][1]] == "1":
                    #adding into the children array dependant on situation
                    if store[j][0] > temp:
                        output.append(parent[:temp]+"1"+parent[temp+1:store[j][0]]+"0"+parent[store[j][0]+1:store[j][1]]+"0"+parent[store[j][1]+1:])
                    else:
                        output.append(parent[:store[j][1]]+"0"+parent[store[j][1]+1:store[j][0]]+"0"+parent[store[j][0]+1:temp]+"1"+parent[temp+1:])
    return output

bfspath = {}
dfspath = {}
def bfs(start):
    #same as my BFSslider, just had to change a few of the method calls

    fringe = deque()
    visited = set()
    fringe.append(tuple([start, 0]))
    visited.add(start)
    #dvisited.append()
    while len(fringe) > 0:
        v = fringe.popleft()
        if v[0] == goalstate:
            return v[1]
        for i in get_children(v[0]):
            if i not in visited:
                visited.add(i)
                fringe.append(tuple([i, v[1]+1]))
                bfspath[i] = v[0]
                # if i == goalstate:
                #     return fringe.pop()[1]
    return None

def dfs(start):
#same as dfs, except pop() instead of popleft()
    fringe = deque()
    visited = set()
    fringe.append(tuple([start, 0]))
    visited.add(start)
    #dvisited.append()
    while len(fringe) > 0:
        v = fringe.pop()
        if v[0] == goalstate:
            return v[1]
        for i in get_children(v[0]):
            if i not in visited:
                visited.add(i)
                fringe.append(tuple([i, v[1]+1]))
                dfspath[i] = v[0]
                # if i == goalstate:
                #     return fringe.pop()[1]
    return None

print(bfs(startstate))

#this part is from the addition of the BFS on wordladder
#this is to trace the path that was mapped throughout the bfs
#had errors in implmeenting them all in the same method, so i took it out
#same as wordladder tho
parent = goalstate
output = []
while(startstate != parent):
    parent = bfspath[parent]
    output.append(parent)
output[-1]
output.append(goalstate)
for i in output:
    format(i)

print(dfs(startstate))

parent2 = goalstate
output2 = []
while(startstate != parent2):
    parent2 = dfspath[parent2]
    output2.append(parent2)
output2[-1]
output2.append(goalstate)
for i in output2:
    format(i)




