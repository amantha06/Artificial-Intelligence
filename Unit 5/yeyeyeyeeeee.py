import sys

dfa1 = sys.argv[1]
dfa2 = sys.argv[2]

start = -1

try:
    start = 0
    listnum = int(dfa1)

except:
    start = 1

if (start == 1):
    with open(dfa1) as file:
        dfa1_list = [line.strip() for line in file]

    ret = dfa1_list[2].split(" ")
    ret = [int(state) for state in ret]
    letlist = dfa1_list[0]
    numlist = int(dfa1_list[1])

with open(dfa2) as file:
    dfa2_list = [line.strip() for line in file]

prob1 = {
    0: {
        "a": 1,
        "b": 4
    },

    1: {
        "a": 2,
        "b": 4
    },

    2: {
        "a": 4,
        "b": 3
    },

    3: {
        "a": 4,
        "b": 4
    },

    4: {
        "a": 4,
        "b": 4
    }
}

prob2 = {
    0: {
        "0": 0,
        "1": 1,
        "2": 0
    },

    1: {
        "0": 0,
        "1": 1,
        "2": 0
    }
}

prob3 = {
    0: {
        "a": 0,
        "b": 1,
        "c": 0
    },

    1: {
        "a": 1,
        "b": 1,
        "c": 1
    }
}

prob4 = {
    0: {
        "0": 1,
        "1": 0
    },

    1: {
        "0": 0,
        "1": 1
    }
}

prob5 = {
    0: {
        "0": 1,
        "1": 2
    },

    1: {
        "0": 0,
        "1": 3
    },

    2: {
        "0": 3,
        "1": 0
    },

    3: {
        "0": 2,
        "1": 1
    }
}

prob6 = {
    0: {
        "a": 1,
        "b": 0,
        "c": 0
    },

    1: {
        "a": 1,
        "b": 2,
        "c": 0
    },

    2: {
        "a": 1,
        "b": 0,
        "c": 3
    },

    3: {
        "a": 3,
        "b": 3,
        "c": 3
    }
}

prob7 = {
    0: {
        "0": 0,
        "1": 1
    },

    1: {
        "0": 2,
        "1": 1
    },

    2: {
        "0": 2,
        "1": 3
    },

    3: {
        "0": 2,
        "1": 4
    },

    4: {
        "0": 4,
        "1": 4
    },
}

prelist = []
prelist.append(("a", "b"))
prelist.append(("0", "1"))
prelist.append(("a", "b"))
prelist.append(("0", "1"))
prelist.append(("0", "1"))
prelist.append(("a", "b", "c"))
prelist.append(("0", "1"))

finlist = []
finlist.append(3)
finlist.append(1)
finlist.append(1)
finlist.append(0)
finlist.append(0)
finlist.append((0, 1, 2))
finlist.append(4)

retlist = []
retlist.append(prob1)
retlist.append(prob2)
retlist.append(prob3)
retlist.append(prob4)
retlist.append(prob5)
retlist.append(prob6)
retlist.append(prob7)

if (start == 1):
    dfa = {}
    count = 0
    dic = {}
    temp = 0

    for line in dfa1_list:
        if (count > 4):
            if (len(line) == 1):
                dic1 = dic.copy()
                dfa[temp] = dic1
                temp = int(line)
                dic.clear()

            elif (len(line) != 0):
                char_toState = line.split(" ")
                newchar = char_toState[0]
                toState = int(char_toState[1])
                dic[newchar] = toState
        if (count == 4):
            temp = int(line)
        count += 1
    dfa[temp] = dic

else:
    dfa = retlist[listnum - 1]
    if (listnum == 6):
        ret = [i for i in finlist[listnum - 1]]
    else:
        ret = [finlist[listnum - 1]]


def parse(test):
    i = 0
    j = 0

    while (i < len(test)):
        ccur = test[i]
        dic = dfa[j]

        if (ccur not in dic):
            return False

        j = dic[ccur]
        i += 1

    if (j in ret):
        return True

    return False


print1 = "*"

try:
    letlist

except:
    letlist = [x for x in prelist[listnum - 1]]

for lts in letlist:
    print1 += "\t" + lts

print(print1)

for i in dfa:
    final_str = str(i)

    for j in letlist:
        if (j not in dfa[i]):
            final_str += "\t" + "_"

        else:
            final_str += "\t" + str(dfa[i][j])

    print(final_str)

print("Final nodes: " + str(ret))
for line in dfa2_list:
    print(str(parse(line)) + " " + line)