import matplotlib.pyplot as plt
import numpy as np

two = 2
one = 1
zero = 0
four = 4
#this is so funny im trolling with these numbers no reason for it
#its cool to just interchange between them
#idk why i just cant wrap my head around it its so odd

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


fig, axs = plt.subplots(4, 4)
fig.suptitle("Graphing Perceptrons - 2024amantha")
#do i need i??
for i, j in enumerate(expand_tt(2)):
    acc, ptron = evaluation(j, 2)

    tx1 = []
    ty1 = []
    tx2 = []
    ty2 = []

    tx1 = [x for x in np.linspace(-2, 2, 20) for y in np.linspace(-2, 2, 20) if
           perceptron(step, ptron[0], ptron[1], [x, y]) > 0.5]
    ty1 = [y for x in np.linspace(-2, 2, 20) for y in np.linspace(-2, 2, 20) if
           perceptron(step, ptron[0], ptron[1], [x, y]) > 0.5]
    tx2 = [x for x in np.linspace(-2, 2, 20) for y in np.linspace(-2, 2, 20) if
           perceptron(step, ptron[0], ptron[1], [x, y]) <= 0.5]
    ty2 = [y for x in np.linspace(-2, 2, 20) for y in np.linspace(-2, 2, 20) if
           perceptron(step, ptron[0], ptron[1], [x, y]) <= 0.5]

    newj = {(int(x), int(y)): int(z) for (x, y), z in j}
    #my truth table is in strings, this turns them into integers and makes it into a dict
    #so it is now easier to call and axess these values

    x_true, y_true, x_false, y_false = [], [], [], []

    for k in newj.keys():
        if newj[k] == one:
            x_true.append(k[zero])
            y_true.append(k[one])
        else:
            x_false.append(k[zero])
            y_false.append(k[one])

    i1, i2 = i//four, i%four

    # Create four polar axes and access them through the returned array
    # fig, axs = plt.subplots(2, 2, subplot_kw=dict(projection="polar"))
    # axs[0, 0].plot(x, y)
    # axs[1, 1].scatter(x, y)
    #from website

    axs[i1,i2].scatter(tx1, ty1, color="magenta", s=3, marker=","); axs[i1,i2].scatter(tx2, ty2, color="cyan", s=3, marker=",")
    axs[i1, i2].scatter(x_true, y_true, color="red", s=40); axs[i1, i2].scatter(x_false, y_false, color="green", s=40)
    axs[i1, i2].set_aspect("equal"); axs[i1, i2].set_adjustable("box")

plt.show()