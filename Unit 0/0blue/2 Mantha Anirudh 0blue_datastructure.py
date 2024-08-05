import heapq
from heapq import heappush, heappop, heapify
import sys 

from time import perf_counter
start = perf_counter()
#All your code goes here, including reading in the files and printing your output

f1, f2, f3 = sys.argv[1], sys.argv[2], sys.argv[3]

with open(f1) as f1:
    list1 = [int(line.strip()) for line in f1]

with open(f2) as f2:
    list2 = [int(line.strip()) for line in f2]

with open(f3) as f3:
    list3 = [int(line.strip()) for line in f3]

set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

#working
print("#1: " + str(len(set1.intersection(set2)) ) )


#working
retlist = []
totsum = 0;

for i in list(dict.fromkeys(list1))[99::100]:
    retlist.append(i)
    totsum += (int)(i)
print("#2: " + str(totsum))
print(retlist)


#working
count = 0
list12 = list1 + list2
for i in list12:
    if(i in set3):
        count += 1
print("#3: " + str(count))


#working
heap = list(map(int, set1))
heapify(heap)
print("#4: " + (str)(heapq.nsmallest(10, heap)))


#NOT WORKING
#list2mod = [i for i in list2 if(not list2mod.contains(list2[i]))]

x = dict()
for i in list2:
    if i not in x:
        x[i] = 1
    else:
        x[i] = x[i] + 1

temp = list()
for i in x:
    if x[i] >= 2:
        temp.append(i)

heap = list(map(int, temp))
heapify(heap)
print("#5: " + (str)(heapq.nlargest(10, heap)))


#Dictionary with the key as the nubmer and the value of frequency
#think about an efficient data strucutre rather than List
#Dictionary has a lot of potential here





#sum = 0
#sixdict = list1
#for index, value in enumerate(sixdict):
#    if value % 53 == 0 and value != 0:
#        minval = min(sixdict[:index])
#        sum = sum + int(minval)
#        print(minval)
#        print(sum)
#        sixdict.remove(minval)

sixset = set()
sixheap = []
sixoutput = []
sum = 0

for i, v in enumerate(list1):
    if v not in sixset:
        sixset.add(v)
        heapq.heappush(sixheap, v)
    if v % 53 == 0:
        temp = heapq.heappop(sixheap)
        sixoutput.append(temp)
        sum = sum + temp

print("#6: " + str(sum))
#print(sixoutput)

end = perf_counter()
print("Total time:", end - start)
