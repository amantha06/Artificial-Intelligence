import sys

two = 2
one = 1
zero = 0

def truth_table(bits, n):

    iterate = two**bits
    initial = [[x for x in bin(i)[two:]] for i in range(iterate)]
    for i in range(len(initial)):
        while len(initial[i]) < bits: initial[i].insert(zero, zero)
    initial = list(reversed(initial))
    num = [x for x in bin(n)[two:]]
    for i in range(len(num)):
        while len(num) < two ** bits: num.insert(zero, zero)
    returnval = []
    for i in range(len(initial)):
        temp = tuple(initial[i])
        newtemp = (temp, num[i])
        returnval.append(newtemp)
    return returnval

def expand_tt(allfactor):
    return [truth_table(allfactor, i) for i in range(two ** (two ** allfactor))]

def pretty_print_tt(table):
    print()
    print("  val  |   out + “\n” + _______|_______" )
    for i in table: print(str(i[0]) + " | " + str(i[1]))

def step(num):
    if num > 0: return 1
    else: return 0

def dot_product(a, b):
    result = sum([a[i] * b[i] for i in range(len(a))])
    return result

def perceptron(A, w, b, x):

    returnval = A(dot_product(w, x) + b)
    if isinstance(returnval, (int, float)): return returnval
    else: raise TypeError("")

def check(n, w, b, truthtabledebuggg):
    #there were two differnt types of truth tables inputted
    if truthtabledebuggg == None: t = truth_table(len(w), n)
    else: t = truthtabledebuggg
    accuracy = 0
    for i in t:
        #this line da problem
        xval = []
        for j in range(len(w)): xval.append(int(i[0][j]))
        xval = tuple(xval)
        retval = perceptron(step, w, b, xval)
        if int(retval) == int(t[t.index(i)][1]): accuracy += 1
    print(accuracy / len(t))
    return accuracy / len(t)

def train(w, t, b):
    returnval = []
    for i in range(100):
        for j in t:
            newj = [int(i) for i in j[0]]
            #HERE IS PROBLEM T[J[0] THINGY
            ptron = perceptron(step, w, b, newj)
            # print(int(t[t.index(j)][1]))
            # print(returnval)
            # input()
            # print(type(t[t.index(j)]))
            # print(type(returnval))
            err = int(t[t.index(j)][1]) - ptron
            #b cannot be made here
            for k in range(len(w)):
                w[k] += one * err * newj[k]
            b = b + (one * err)
        returnval.append((tuple(w), b))
        if 1 < len(returnval):
            #if last two are same
            if returnval[-2] == returnval[-1]: return returnval[-2]
    return returnval[-1]

def evaluation(t, n):
    ptron=train([0]*n, t, 0)
    accuracy=check(n, ptron[0], ptron[1], t)
    return accuracy, ptron

inputvalues = sys.argv[1:]

bits, num = int(inputvalues[0]), int(inputvalues[1])
table = truth_table(bits, num)

accuracy, ptron = evaluation(table, bits)
print(ptron)
print(accuracy)
print(num)
