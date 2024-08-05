import sys
import math
import numpy as np

zero = 0
one = 1
two = 2

def A(n): return 1 / (1 + np.e**-n)

def dot_product(a, b):
    result = sum([a[i] * b[i] for i in range(len(a))])
    return result

def perceptron(A, w, b, x):
    returnval = A(dot_product(w, x) + b)
    if isinstance(returnval, (int, float)): return returnval
    else: raise TypeError("")

def perceptron_network(A_vec, weights, biases, input):
    #let a be a Python list of numpy matrices that will hold the output at each layer
    returnval = [np.reshape(input, (-1, 1))]
    for i in range(one, len(weights)): returnval.append(A_vec((weights[i] @ returnval[i-one]) + biases[i]))
    return returnval[-1]

def train_two(w, b, e, t):
    A_vec = np.vectorize(A)
    for i in range(e):
        for j in t:
            x, y = j
            aval, dott, d, lam, num = [x], [None], [None]*len(w), 0.1, len(w)-1
            for k in range(1, num+1):
                aval.append(A_vec((w[k]@aval[k-1])+b[k]))
            d[num] = (aval[num] * (1 - aval[num])) * (y-aval[num])
            #forward prop
            for k in range(num-1, 0, -1):
                d[k] = (aval[k] * (1-aval[k])) * (w[k+1].T @ d[k+1])
            #back prop
            for k in range(1, len(w)):
                w[k] = w[k] + (lam * (d[k] @ aval[k-1].T))
                b[k] = b[k] + lam * d[k]
            #update
            print(aval[num])
        #print()
    return w, b, aval

def sum_net():
    w, b = [None], [None]
    epochs = 10000

    traindata = [
        (np.array([[0], [0]]), np.array([[0], [0]])),
        (np.array([[0], [1]]), np.array([[0], [1]])),
        (np.array([[1], [0]]), np.array([[0], [1]])),
        (np.array([[1], [1]]), np.array([[1], [0]]))
    ]

    array1 = np.array([[np.random.uniform(-1, 1), np.random.uniform(-1, 1)], [np.random.uniform(-1, 1), np.random.uniform(-1, 1)]])
    w.append(array1)

    array2 = np.array([[np.random.uniform(-1, 1), np.random.uniform(-1, 1)], [np.random.uniform(-1, 1), np.random.uniform(-1, 1)]])
    w.append(array2)

    b.append(np.array([[np.random.uniform(-1, 1)], [np.random.uniform(-1, 1)]]))
    b.append(np.array([[np.random.uniform(-1, 1)], [np.random.uniform(-1, 1)]]))

    returnval = train_two(w, b, epochs, traindata)
    print(perceptron_network(np.vectorize(A), returnval[0], returnval[1], np.array([[1],[1]])))

def circle_net():
    epochs = 500
    w, b = [None], [None]

    values = [
        2 * np.random.rand(12, 2) - 1,
        2 * np.random.rand(4, 12) - 1,
        2 * np.random.rand(1, 4) - 1
    ]

    w.extend(values)

    values = [
        2 * np.random.rand(12, 1) - 1,
        2 * np.random.rand(4, 1) - 1,
        2 * np.random.rand(1, 1) - 1
    ]

    b.extend(values)

    traindata = []
    with open("10000_pairs.txt") as file1:
        for i in file1:
            x, y = i.split()
            temp = np.array([[float(x)], [float(y)]])
            #there have to be seperate not together or else ran into pa
            decision = 1 if math.sqrt(temp[0] ** 2 + temp[1] ** 2) < 1 else 0
            traindata.append((temp, np.array([[decision]])))
    #traindata is from textfile instead of like it was before
    returnval = train_three(w, b, epochs, traindata)

    return returnval[0], returnval[1]


def train_three(w, b, e, t):
    lam = 0.1; A_vec = np.vectorize(A)
    for i in range(e):
        store_error = []
        for j in t:
            x, y = j
            aval, dott, d, num = [x], [None], [None]*len(w), len(w)-1
            for k in range(1, num+1):
                aval.append(A_vec((w[k] @ aval[k-1]) + b[k]))
            store_error.append(0.5*((np.sum(np.square((y - aval[num]))))) ** 0.5)
            d[num] = (aval[num] * (1-aval[num])) * (y-aval[num])

            for k in range(num-1,0,-1):
                d[k] = (aval[k] * (1-aval[k])) * (w[k+1].T @ d[k+1])
            for k in range(1, num+1):
                w[k] = w[k] + (lam * (d[k] @ aval[k-1].T))
                b[k] = b[k] + (lam * d[k])
        #adjust lambda so the misclassified stop getting bounced around
        numerator = 0
        for j in store_error:
            numerator += j

        lam = numerator/len(store_error)

        countmiscout = lambda A_vec, w, b, t: sum(1 for x, y in t if y[0, 0] != (1 if perceptron_network(A_vec, w, b, x)[0, 0] > 0.5 else 0))
        print("epoch", i, "num of inaccurate:", countmiscout(A_vec, w, b, t))

    print("weight ", w, " | bias ", b)
    return w, b




if sys.argv[1] == "S":
    sum_net()

if sys.argv[1] == "C":
    circle_net()

