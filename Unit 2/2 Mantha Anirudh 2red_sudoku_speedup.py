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


#NEEDS SLIGHT MODIFICATION FOR FORWARD LOOKING

# def pos_values(strboard, index):
#      ret_values = set()
#      n_values = set()
#      for i in neighbor[index]:
#           if strboard[i] != blank:
#                n_values.add(strboard[i])
#      for i in symbol_set:
#           if i not in n_values:
#                ret_values.add(i)
#      return list(sorted(ret_values))

def pos_values(strboard):
     board_possible = []
     #there should be a way to make this all one line
     for i in range(len(strboard)):
          board_possible.append("")
          #adding placeholder value so you can just tatch on a value at the end
          neighbor_values = {strboard[n] for n in neighbor[i]}
          values = {s for s in symbol_set if s not in neighbor_values}
          board_possible[i] = "".join(sorted(values))
          #cannot just append the sorted values into the list directly or else there is an error
     return board_possible


#input the board and a list of potentials
def for_looking(strboard, potential):

     #if there is only 1 possible value in the board
     return_success = [i for i in potential if len(strboard[int(i)]) == 1]

     while len(return_success) > 0:
     #going through all possible values
          i = return_success[0]
          return_success.remove(i)
          ##cant pop left??

          v = strboard[i]
          for n in neighbor[i]:
               if v in strboard[n]:
                    strboard[n] = strboard[n].replace(v, "")
                    if len(strboard[n]) == 1: return_success.append(n)
                         #putting that number into the "box"
                         #can be multiple i.e. if there can be a 3 and 5 in a box
                         #this list woudl have 3 and 5
     for i in strboard:
          if len(i) == 0:
               return None
     #if there are no possible values that can fit
     return strboard



def csp_backtracking_with_forward_looking(strboard):
     # VERY VERY VERY SIMILAR TO PSUEDO
     retval_of_first_part = None
     ind = {}
     for i in range(len(strboard)):
         if len(strboard[i]) > 1:
              ind[i] = len(strboard[i])
     if len(ind) == 0: retval_of_first_part = None
     else:
         #dict OP
         small = min(ind.values())
         for i in ind:
              retval_of_first_part = i
              if ind[i] == small: break

     #RET VAL OF FIRST PART IS GETTING THE MOST CONSTRAINTED BLOCK/ROW/LINE
     temp = retval_of_first_part
     #get the one with most problems
     if temp == None:
          return strboard
     #if there is nothing just return and go for next one
     sett = set()
     for i in neighbor[temp]:
          sett.add(i)
     sett.add(temp)

     sortedboard = sorted(strboard[temp])
     for i in sortedboard:
          updated = strboard.copy()
          #DO NOT USE COPY.DEEPCOPY
          updated[temp] = i
          verify = for_looking(updated, sorted(sett))
          #for looking needs the set and this gives that set
          #recursion! yay!

          if verify is not None:
               result = csp_backtracking_with_forward_looking(verify)
               if result is not None:
                    return result
     return None

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
     tobesolved = pos_values(i)

     firststep = for_looking(tobesolved, [i for i in range(len(tobesolved))])

     solved = csp_backtracking_with_forward_looking(firststep)
     display(solved)
     #print("".join(solved))

#print(perf_counter() - start)
