import sys
import ast
import numpy as np
import math

def demo():
    # A demonstration of amazing things in numpy that make working with matrices soooooo easy!
    x = np.array([[0, 3], [3, 4]])
    print("Matrix x:")
    print(x)
    print()

    y = np.array([[4, 5], [-1, -2]])
    print("Matrix y:")
    print(y)
    print()

    print("The element of matrix y at row 1, column 0 is:")
    print(y[1, 0])  # NOTE this is NOT y[1][0] - item access syntax is NOT the same as lists of lists
    print()

    print("Dot product:")
    print(x@y)
    print()

    print("Item-wise product:")  # DO NOT GET THIS CONFUSED WITH THE DOT PRODUCT!
    print(x*y)
    print()

    print("Item-wise sum:")
    print(x+y)
    print()

    print("Scalar multiplication:")
    print(3*x)
    print()

    print("...or:")
    print(x*3)
    print()

    print("Add a value to every value in a matrix:")
    print(x + 3)
    print()

    print("Transpose:")
    print(y.transpose())
    print()

    print("...or:")
    print(y.T)
    print()

    print("Create an array of zeroes:")
    print(np.zeros((2, 3)))
    print()

    print("Create an array of random values on the interval [0,1):")
    print(np.random.rand(2, 3))  # Note this takes two integer args where "zeroes" takes a tuple
    print()

    print("Create an array of random values on the interval [-1,1):")
    new_arr = 2 * np.random.rand(2, 3) - 1  # Why does this work?
    print(new_arr)
    print()

    print("Find the magnitude of a column vector:")
    vec = np.array([[3], [-4]])  # Vector represented as a 2-d matrix with a single column
    mag = np.sum(np.square(vec)) ** 0.5  # np.square is itemwise squaring, np.sum adds the values
    print("Magnitude of this vector:\n%s\nis %s." %(vec, mag))
    print()

    print("Vectorize a function:")
    # This is the step function, defined with a single numeric input and a single numeric output
    #print(f(x))  # If you uncomment this, it will throw an error!  The original function cannot accept a matrix as an argument
    new_f = np.vectorize(f)  # This creates a function that applies the original function to each element of a matrix individually
    print(new_f(x))
    print()

    # NOTE: np.vectorize makes pretty slow functions; it's worth noting that the step function needs to be vectorized
    # because of the "if n > 0" part, but built in numpy broadcasting works on any purely mathematical operations.
    # So, check this out:
     # This is an activation function we'll use a little later on; the sigmoid function.
    print("This function doesn't need to be vectorized:")
    print(A(x))

two = 2
one = 1
zero = 0




def perceptron_network(A_vec, weights, biases, input):
    #let a be a Python list of numpy matrices that will hold the output at each layer
    returnval = [np.reshape(input, (-1, 1))]
    for i in range(one, len(weights)): returnval.append(A_vec(weights[i] @ returnval[i-one] + biases[i]))
    return returnval[-1]

def circle_challenge(A_vec, weights, biases):
    accuracy = 0
    for i in range(500):
        in_ = np.random.random((2,)) * 2 - 1
        determiner = math.sqrt(in_[0]**2 + in_[1]**2)
        #circle formula, will do operations based off of waht the value is +- 1
        pnet = perceptron_network(A_vec, weights, biases, in_)
        #this if statement took like 5 years to figure out
        if (determiner < 1 and pnet[0,0] > 0.5) or (determiner >= 1 and pnet[0,0] <= 0.5): accuracy = accuracy + 1
        else: print("i, j", in_, "   accuracy, ", pnet[0,0])

    return accuracy/500


A_vec = np.vectorize(A_vec)
w, b = [None], [None]
if len(sys.argv[1:]) == 1:
    #XOR HAPPENS HERE
    w.extend([np.array([[-1, 1], [1, -1]]), np.array([[1, 1]])]); b.extend([np.array([[0, 0]]), np.array([[0]])])
    #i = (np.array([1, 1]), np.array([1, 0]), np.array([0, 1]), np.array([0, 0]))
    #i is for showing the inputs
    print(perceptron_network(A_vec, w, b, np.array(ast.literal_eval(sys.argv[1])))[0,0])
elif len(sys.argv[1:]) == 2:
    w.extend([np.array([[1, 1], [-1, -1], [1, -1], [-1, 1]]), np.array([[1, 1, 1, 1]])]); b.extend([np.array([[1, 1, 1, 1]]), np.array([[-3]])])
    if perceptron_network(A_vec, w, b, ((np.array([float(sys.argv[1:][0])])), (np.array([float(sys.argv[1:][1])]))))[0,0] > 0.5: print("inside")
    else: print("outside")
elif sys.argv[1:] == "demo":
    demo()
else:
    w.extend([np.array([[1, 1], [-1, -1], [1, -1], [-1, 1]]), np.array([[1, 1, 1, 1]])]); b.extend([np.array([[0.84], [0.84], [0.84], [0.84]]), np.array([[-1.35]])])
    print("i =",0.85, " j =",-1.35, "has an accuracy of ", circle_challenge(A, w, b))

