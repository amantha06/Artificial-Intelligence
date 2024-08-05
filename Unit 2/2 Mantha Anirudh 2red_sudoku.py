import heapq
from collections import deque
from time import perf_counter
from heapq import heappush, heappop, heapify
import sys

f1 = sys.argv[1]
with open(f1) as f:
    line_list = [line.strip() for line in f]

def constraint_sets():
     w = subblock_width
     h = subblock_height
     c_list = []
     rowlist = [{(x*n+y) for y in range(n)} for x in range(n)]
     for i in rowlist:
          c_list.append(i)

     collist = [{(x+y*n) for y in range(n)} for x in range(n)]
     for i in collist:
          c_list.append(i)
     #worked out in full form, then simplified in list comprehension
     blocklist = [[(x*n+y) for x in range(h * (x2-1), h*x2) for y in range(w * (y2 - 1), w * y2)] for x2 in range(1, w + 1) for y2 in range(1, h + 1)]
     for i in blocklist:
          c_list.append(i)
     return c_list

#did row, then col, then block
#each one is its own row
#block was a list not a set
#list comprehension really simplified the code
#the ranges of the for loops had to go from 1 - h+1, because of indexing errors
#^annoying to debug

def neighbors(const):
     neighbor_list = [{i for c in const if j in c for i in c if i != j} for j in range(n**2)]
     return neighbor_list

def symbol_check(strboard):
     for i in symbol_set:
          cnt = sum([j.count(i) for j in strboard])
          print(i, "-", cnt)

def pos_values(strboard, index):
     ret_values = set()
     n_values = set()
     for i in neighbor[index]:
          if strboard[i] != blank:
               n_values.add(strboard[i])
     for i in symbol_set:
          if i not in n_values:
               ret_values.add(i)
     return sorted(ret_values)

def backtracking(strboard):
     if blank not in strboard:
          return strboard
     temp = strboard.index(blank)
     for i in pos_values(strboard, temp):
          updated = strboard[:temp] + str(i) + strboard[temp+1:]
          returnval = backtracking(updated)
          if returnval != None:
               return returnval
     return None
#basic backtracking alg


def readfile_info(strboard):
     n = int(len(strboard)**0.5)
     symbol_set = set()
     letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

     if n <= 9:
          for i in range(1, n+1):
               symbol_set.add(str(i))
     #if the size is greater than a single digit number
     #then the next number is the index of the string "letters"
     #basically 10 is A, 11 is B etc...
     else:
          for i in range(n-9):
               symbol_set.add(str(letters[i]))
          for i in range(1, 10):
               symbol_set.add(str(i))


     for i in range(int(n**0.5), n):
          if n % i == 0:
               subblock_h_w = sorted([i, int(n/i)])
               subblock_width = int(subblock_h_w[0])
               subblock_height = int(subblock_h_w[1])
               return n, subblock_width, subblock_height, symbol_set


def display(strboard):
     w = subblock_width
     h = subblock_height
     #simplifies code a lot
     for r in range(n):
          #height component
          if r % h == 0:
               print("_____________________________")
              #new line
          for i in range(subblock_height):
               #printing from the left boudn to the right bound
               print("  ".join(strboard[(n * r + i * w):(n * r + (i + 1) * w)]), end=" | ")
          print()
     print("__________END BOARD_________")
#end is used so that the sections are in their right box
#the random print statements are after debugging to make the board look right

start = perf_counter()
for i in line_list:
     blank = "."
     n, subblock_height, subblock_width, symbol_set = readfile_info(i)
     #step 1 in doc
     constraints = constraint_sets()
     neighbor = neighbors(constraints)
     solved = backtracking(i)
     print("".join(solved))
     #display(solved)
#print(perf_counter() - start)