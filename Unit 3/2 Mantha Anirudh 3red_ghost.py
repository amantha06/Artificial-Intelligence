import sys
from time import perf_counter
start = perf_counter()

words_set = set()
f1 = sys.argv[1]
lmin = int(sys.argv[2])

# f1 = "words_all.txt"
# lmin = 4

even = "E"
odd = "O"

def isEven(input):
    if input % 2 == 0: return even
    else: return odd

#base condition seeing number of inputs
if len(sys.argv) < 4: starting = ""
else: starting = sys.argv[3]
# starting = "AB"
with open(f1) as f:
    words_list = [i.strip() for i in f]
for i in words_list:
    if i.isalpha() and lmin <= len(i):
        words_set.add(i.upper())
#getting the words in the set
#for easy membership testing later on for dictionary

words_dict = {}
for i in words_set:
    words_dict[i] = [None]
    for j in range(len(i)-1):
        if i[:j+1] in words_dict:
            temp = words_dict[i[0:j+1]]
            #adding value to the key
            if i[:j+2] not in temp: words_dict[i[:j+1]].append(i[:j+2])
        else: words_dict[i[:j+1]] = [i[:j+2]]
#makes dictionary so in apple A - AP; AP - APP; APP - APPL; APPL - APPLE... BUT APPLE !-> APPLES
for i in words_set:
    if i in words_dict:
        words_dict[i] = []
#cant do list comprehension cause dictionary is already made



e_or_o = None
if isEven(len(starting)) == even: e_or_o = even
else: e_or_o = odd
#know how far game needs to go

def score(current_word):
    if current_word in words_set:
        if (isEven(len(current_word)) == even and e_or_o == even) or (isEven(len(current_word)) == odd and e_or_o == odd): return 1
        else: return -1

def possible_moves(current_word):
    if current_word == "":
        # retlist = []
        # for i in "abcdefghijklmnopqrstuvwxyz":
        #     retlist.append(str(i))
        # return retlist
        return [str(i) for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    else:
        return words_dict[current_word]
#getting the next string
#APP -> APPL not L
#this was a problem i had during the challenge itself
#this way its also easier to toss around through min and max

def max_step(current_word):
    if score(current_word) != None:
        return score(current_word)
    retlist = [min_step(i) for i in possible_moves(current_word)]
    return max(retlist)


def min_step(current_word):
    if score(current_word) != None:
        return score(current_word)
    retlist = [max_step(i) for i in possible_moves(current_word)]
    return min(retlist)


def play():
    retlist = []
    for i in possible_moves(starting):
        scored = min_step(i)
        if scored == 1:
            if len(i) >= 2: retlist.append([i[-1]])
                #get the last letter of that string to get the actual move
            else: retlist.append([i])

    if len(retlist) == 0: print("Next player will lose!")
    else: print("Next player can guarantee victory by playing any of these letters: ", retlist)

play()
#print(perf_counter()-start)

#the main mistake I made in class, was to make the dictionary A -> APPLE; NOW it does A -> AP, and I can easily access the lastest character