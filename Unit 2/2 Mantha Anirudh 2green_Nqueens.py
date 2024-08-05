import sys
from heapq import heappop, heappush, heapify
from time import perf_counter

testcase1 = [None] * 6
def test_solution(state):
    for var in range(len(state)):
        left = state[var]
        middle = state[var]
        right = state[var]
    for compare in range(var + 1, len(state)):
        left -= 1
        right += 1
        if state[compare] == middle:
            print(var, "middle", compare)
            return False
        if left >= 0 and state[compare] == left:
            print(var, "left", compare)
            return False
        if right < len(state) and state[compare] == right:
            print(var, "right", compare)
            return False
    return True


def check(state):
    for i in state:
        if i is not None:
            return True
    return False

def get_sorted_values(state, row):
    pset = set()
    plist = []
    for i in range(len(state)):
        temp = abs(row - i)
        if not state[i] == None:
            pset.add(state[i])
            if state[i] != 0 and state[i] != len(state)-1:
                pset.add(state[i]-temp)
                pset.add(state[i]+temp)
            if state[i] == 0:
                pset.add(state[i] + temp)
            if state[row] == len(state)-1:
                pset.add(state[i] - temp)
    for i in range(1, len(state)+1):
        if i%2 == 0:
            if (len(state) - i//2) not in pset:
                plist.append(len(state) - i//2)
            else:
                if i//2 not in pset:
                    plist.append(i//2)
    return plist


def get_next_unassigned_var(state):
    returnval = 0
    storeval = len(state)
    for i in range(len(state)):
        if state[i] == None:
            temporaryvar = abs(len(state)//2-i)
            if temporaryvar <= storeval:
                returnval = i
                storeval = temporaryvar
    return returnval


def csp_backtracking(state):
    if check(state):
        return state
    temp = get_next_unassigned_var(state)
    for i in get_sorted_values(state, temp):
        newval = state.copy()
        newval[i] = i
        returnval = csp_backtracking(newval)
        if returnval is not None:
            return returnval
    return None

start = perf_counter()

print("board: ", str(csp_backtracking(testcase1)))
print(str(perf_counter()-start))