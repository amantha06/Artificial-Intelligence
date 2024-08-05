import random
import time
start = time.perf_counter()

testcase1 = [None] * 33
testcase2 = [None] * 37
testcase3 = [None] * 41

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

def num_of_conflicts(state):
    count = 0
    clist = []
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if (abs(j - i) == abs(state[j] - state[i])) or state[j] == state[i]:
                clist.append((i, j))
                count += 1
    return count, clist


def get_incorrect_row(state):
    count, clist = num_of_conflicts(state)
    countlist = [0] * len(state)
    for i in range(len(clist)):
        firstc = clist[i][0]
        secondc = clist[i][1]
        countlist[firstc] += 1
        countlist[secondc] += 1
    largestc = max(countlist)
    largestlist = []
    for i in range(len(countlist)):
        if(countlist[i] == largestc):
            largestlist.append(i)
            #adding the largest value to its designated list
    return random.choice(largestlist)

def get_least_attacking_queen(state, row):
    countlist = []
    for i in range(len(state)):
        count = 0
        for j in range(len(state)):
            if i == state[j]:
                count += 1
            if abs(state[j] - i) == abs(j - row):
                count += 1
        countlist.append(count)
    smallestc = min(countlist)
    smallestlist = []
    for i in range(len(countlist)):
        if(countlist[i] == smallestc):
            smallestlist.append(i)

    return random.choice(smallestlist)

def inc_repair(state):
    while num_of_conflicts(state)[0] != 0:
        incorrectrow = get_incorrect_row(state)
        leastattacking = get_least_attacking_queen(state, incorrectrow)
        state[incorrectrow] = leastattacking
        print("Current State: ", state, " with ", num_of_conflicts(state)[0], "conflicts")
    return state


#THERE HAS TO BE AN EASIER WAY TO DO THIS
#I OVERCOMPLICATED THIS BUT IT'LL DO FOR NOW
choices = [i for i in range(len(testcase1))]
for i in range(len(testcase1)):
    randomv = random.choice(choices)
    testcase1[i] = randomv
    choices.remove(randomv)

print("Initial State:", testcase1)
print("Final State:", inc_repair(testcase1))
print("Is it valid?", test_solution(inc_repair(testcase1)))

choices = [i for i in range(len(testcase2))]
for i in range(len(testcase2)):
    randomv = random.choice(choices)
    testcase2[i] = randomv
    choices.remove(randomv)

print("Initial State:", testcase2)
print("Final State:", inc_repair(testcase2))
print("Is it valid?", test_solution(inc_repair(testcase2)))

end = time.perf_counter()
print('Time taken:', end-start, 'seconds')