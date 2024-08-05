from time import perf_counter
start = perf_counter()


def is_prime(n):
    istrue = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            istrue = False
            break

    return istrue

def fib(n):
    x, y = 0, 1
    for i in range(0, n):
        x, y = y, x + y
    return x

def factor(n):
    #computational formula to get number of factors
    factors = 0
    for i in range (1, int(n**0.5)):
        if n % i == 0:
            factors += 1
    return (factors * 2)

def collatz(num):
    length = 0
    store = num
    #for all unfamiliar values
    while store not in seq:
        if store % 2 == 0:
            store=store/2
        else:
            store = 3*store + 1
        length += 1

    #storing all values in a dictionary to always refer to incase that number comes again
    #saves a lot of time
    #dictionary is used to implement this
    seq[num] = length + seq[store]


def recurmethod(x, y, tot):

    tot = tot + data2[x][y]

    if x == 14:
        potentialsum.append(tot)
    else:
        recurmethod(x + 1, y, tot)
        recurmethod(x + 1, y + 1, tot)

def factorslist(n):
    factorlist = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            factorlist.append(i)
            factorlist.append(n//i)

    return factorlist

def gcd(x, y):
    if y == 0:
        return int(x)
    else:
        return gcd(y, x%y)


num_string = "73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450"


data = [[ 8,  2, 22, 97, 38, 15,  0, 40,  0, 75,  4,  5,  7, 78, 52, 12, 50, 77, 91,  8],

       [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48,  4, 56, 62,  0],

       [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30,  3, 49, 13, 36, 65],

       [52, 70, 95, 23,  4, 60, 11, 42, 69, 24, 68, 56,  1, 32, 56, 71, 37,  2, 36, 91],

       [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],

       [24, 47, 32, 60, 99,  3, 45,  2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],

       [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],

       [67, 26, 20, 68,  2, 62, 12, 20, 95, 63, 94, 39, 63,  8, 40, 91, 66, 49, 94, 21],

       [24, 55, 58,  5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],

       [21, 36, 23,  9, 75,  0, 76, 44, 20, 45, 35, 14,  0, 61, 33, 97, 34, 31, 33, 95],

       [78, 17, 53, 28, 22, 75, 31, 67, 15, 94,  3, 80,  4, 62, 16, 14,  9, 53, 56, 92],

       [16, 39,  5, 42, 96, 35, 31, 47, 55, 58, 88, 24,  0, 17, 54, 24, 36, 29, 85, 57],

       [86, 56,  0, 48, 35, 71, 89,  7,  5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],

       [19, 80, 81, 68,  5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77,  4, 89, 55, 40],

       [ 4, 52,  8, 83, 97, 35, 99, 16,  7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],

       [88, 36, 68, 87, 57, 62, 20, 72,  3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],

       [ 4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18,  8, 46, 29, 32, 40, 62, 76, 36],

       [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74,  4, 36, 16],

       [20, 73, 35, 29, 78, 31, 90,  1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57,  5, 54],

       [ 1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52,  1, 89, 19, 67, 48]]

data2 = [[75],

       [95, 64],

       [17, 47, 82],

       [18, 35, 87, 10],

       [20,  4, 82, 47, 65],

       [19,  1, 23, 75,  3, 34],

       [88,  2, 77, 73,  7, 63, 67],

       [99, 65,  4, 28,  6, 16, 70, 92],

       [41, 41, 26, 56, 83, 40, 80, 70, 33],

       [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],

       [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],

       [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],

       [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],

       [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],

       [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]

breakoutloop = False



#Problem 1:
print(sum(i for i in range(1000) if i%3 == 0 or i%5 == 0))
###


#Problem 2:
list1 = []
x, y = 0, 1
for i in range(0, 1000):
    x, y = y, x + y
    if(x > 4000000):
        break
    list1.append(x)
print(sum(i for i in list1 if i % 2 == 0))
###


#Problem 3:
pfactoroutput = []
for i in factorslist(600851475143):
    if is_prime(i):
        pfactoroutput.append(i)
print(max(pfactoroutput))
###


#Problem 4: 906609
maxpal = 0
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        s = i*j
        if str(s) == str(s)[::-1]:
            if s > maxpal:
                maxpal = s
print(maxpal)
###

#Problem 5

testlist = range(1,21)
lcm = 1
for i in testlist:
    div = lcm*i
    diz = gcd(lcm, i)
    lcm = div//diz
print(lcm)

###


#Problem 6:
print(sum(i for i in range(101))**2 - sum(j**2 for j in range(101)))
##

#Problem 7
count = 2
for i in range(5, 1000000, 2):
    if is_prime(i):
        count+=1

        if(count == 10001):
            print(i)
            break
###


#Problem 8
check = 0
for i in range(len(num_string)-13):
    tot = 1
    for j in num_string[i:i+13]:
        tot *= int(j)
    if tot > check:
        check = tot
print(check)
###


#Problem 9
breakoutloop = False
tripleprod = 0
for x in range(1, 1000):
    for y in range(1, 1000):
        z = -(y + x) + 1000
        if x**2 + y**2 == z**2:
            tripleprod = x*y*z
            breakoutloop = True
            break

    if breakoutloop == True:
        break
print(tripleprod)
###



#Problem 11
maxprod = 0
for x in range (0, 20):
    for y in range (0, 16):
        downprod = data[x][y] * data[x][y+1] * data[x][y+2] * data[x][y+3]
        maxprod = max(maxprod, downprod)

for x in range (0, 16):
    for y in range (0, 20):
        acrossprod = data[x][y] * data[x+1][y] * data[x+2][y] * data[x+3][y]
        maxprod = max(maxprod, acrossprod)

for x in range (0, 16):
    for y in range (0, 16):
        diagprod = data[x][y] * data[x+1][y+1] * data[x+2][y+1] * data[x+3][y+1]
        maxprod = max(maxprod, diagprod)

for x in range (0, 16):
    for y in range (4, 20):
        diagoppprod = data[x][y] * data[x+1][y-1] * data[x+2][y-2] * data[x+3][y-3]
        maxprod = max(maxprod, diagoppprod)

print(maxprod)
###



#Problem 12

triangle = 0
increment = 1
numfactors = 0
#while loop because you dont know where to stop

while numfactors < 500:
    numfactors = 0
    #update triangle number
    #update incremental value
    triangle += increment
    increment += 1
    #for loop without a forloop
    numfactors = factor(triangle)
print("adfasdlkfjlaksdfj " + str(triangle))
#print(factor(76576500))
###


#Problem 14
seq = {1:1}
maxval = seq[1]
answer = 0

for i in range(2, 1000000):
    if i not in seq.keys():
        collatz(i)
    if seq[i] > maxval:
        maxval = seq[i]
        answer = i
print(answer)
###



#Problem 18
#iterative approach, somewhere gone wrong, best way to tackle problem is recursion
#y = 0
#totval = 75
#for x in range(1, 15):
#    if data2[x][y] > data2[x][y+1]:
#        print(data2[x][y])
#        input()
#        totval += data2[x][y]
#    else:
#        print(data2[x][y+1])
#        input()
#        totval += data2[x][y+1]
#        y += 1
# OUTPUT: 1064, am I not adding 10 somewhere??

#Problem 18
potentialsum = []
recurmethod(0, 0, 0)
print(max(potentialsum))
###


#Problem 28
#rows, cols = (11, 11)
#grid = [[0 for i in range(cols)] for j in range(rows)]
#grid[rows//2][cols//2] = 1
#for i in range(rows**2):
###


#Problem 29
print(len(set(a**b for a in range(2, 101) for b in range(2, 101))))
###


end = perf_counter()
print("Total time:", end - start)



