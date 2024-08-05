import sys
import ast


def truth_table(bits, n):
    two = 2
    zero = 0
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


def pretty_print_tt(table):
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

def check(n, w, b):
    accuracy = 0
    t = truth_table(len(w), n)
    for i in t:
        #this line da problem
        xval = []
        for j in range(len(w)): xval.append(int(i[0][j]))
        xval = tuple(xval)
        retval = perceptron(step, w, b, xval)
        if int(retval) == int(t[t.index(i)][1]): accuracy += 1
    print(accuracy / len(t))
    return accuracy / len(t)


inputvalues = sys.argv[1:]
check(int(inputvalues[0]), ast.literal_eval(inputvalues[1]), float(inputvalues[2]))

