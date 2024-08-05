import pickle
import numpy as np
import scipy


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

def testsdata(w, b, t):
    counter = 0
    for i in t:
        perceptron_output = perceptron(A, i[0], w, b)
        max_index = np.argmax(perceptron_output)
        if max_index != np.where(i[1] == 1)[1][0]: counter += 1
    return counter/len(t)
#same as backprop
def train(w, b, e, t):
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

        #PICKEL TIME
        file1 = open("anirudhtrain.pkl", "wb")
        pickle.dump((w, b), file1)
        file1.close()

        numerator = 0
        for j in store_error:
            numerator += j
        #lam = numerator/len(store_error)
        #makes go down
        countmiscount = lambda w, b, e, t: \
            print("epoch", e, ": misclassified: ", sum(
                np.argmax(perceptron(A_vec, p[0], w, b)) != np.where(p[1] == 1)[1][0] for p in t) / len(t))
        #print("epoch", i, "misclassified: ", countmiscount(w, b, i+1, t))

    #print("weight ", w, " | bias ", b)
    return w, b


zero, one, two = 0,1,2
# datatrain = []
# with open("mnist_train.csv") as file:
#     for i in file:
#         i = i.strip().split(",")
#         x, y = np.empty((one, 784)), np.array([[zero,zero,zero,zero,zero,zero,zero,zero,zero,zero]])
#         y[0, int(i[0])] = 1
#         for j in range(1, len(i)):
#             x[0, j-1] = int(i[j])/255
#         datatrain.append(([x], [y]))
#
# file1 = open("anirudhtrain.pkl", "wb")
# pickle.dump(datatrain, file1)
# file1.close()

# file1 = open("anirudhtrain.pkl", "rb")
# datatrain = pickle.load(file1)

w, b = [None], [None]
values = [
    two * np.random.rand(784, 300) - one,
    two * np.random.rand(300, 100) - one,
    two * np.random.rand(100, 10) - one
]
w.extend(values)

values = [
    two * np.random.rand(1, 300) - one,
    two * np.random.rand(1, 100) - one,
    two * np.random.rand(1, 10) - one
]

b.extend(values)

#w, b = train(w, b, 125, datatrain)
#no need anymore

testset = []
with open("mnist_test.csv") as file:
    for i in file:
        i = i.strip().split(","); x, y = np.empty((one, 784)), np.array([[zero,zero,zero,zero,zero,zero,zero,zero,zero,zero]]); y[0, int(i[0])] = 1
        for j in range(1, len(i)): x[0, j-1] = int(i[j])/255
        testset.append(([x], [y]))

        jitter = np.random.randint(0, 7)
        if jitter == 0: temp = [float(j) / 255 for j in i[2:].split(',')]
        elif jitter == 1 or jitter == 2:
            ini = ini[2:].strip().split(',')
            returnval = []
            for x in range(28):
                k = 0
                start_index = 28 * k
                end_index = 28 * (k + 1)
                pix = ini[start_index:end_index]
                r = np.array([float(i) / 255 for i in pix])
                r = np.roll(r, -1) if jitter == 1 else np.roll(r, 1)
                returnval.append(r)
            temp = np.array(returnval)
        elif jitter in [3, 4, 5, 6]:
            ini = ini[2:].strip().split(',')
            returnval = []
            for x in range(28):
                row_list = np.array([float(i) / 255 for i in ini[28 * x: 28 * (x + 1)]])
                returnval.append(row_list)
            temp = np.array(returnval)
            if jitter == 3: temp = scipy.ndimage.rotate(temp, -15, reshape=False)
            elif jitter == 4:  temp = np.roll(temp, 1, axis=0)
            elif jitter == 5: temp = scipy.ndimage.rotate(temp, 15, reshape=False)
            elif jitter == 6: temp = np.roll(temp, -1, axis=0)

        temp = np.reshape(temp, (784, 1))
        finalreturnvalue = temp

        #reshape everythign at the end
        #otherwise causes errors
        testset.append((finalreturnvalue, y))

filetesting = open("anirudhtrain.pkl", "rb")
tset = pickle.load(filetesting)

print("test data miscalculation error: ", testsdata(tset[0], tset[1], testset))


# print("network arc: ", [784, 300,100,10])
# print("epochs used: ", 125)
#realistically only needed 100
