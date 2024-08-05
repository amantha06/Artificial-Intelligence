import sys
import math

def delta_s(s, g):

    returnval = {}
    returnval_group = g[-1]
    for i in s:
        if i[returnval_group] not in returnval: returnval[i[returnval_group]] = 1
        else: returnval[i[returnval_group]] += 1
    dS = 0
    for i in returnval: dS += (returnval[i]/len(s)) * math.log2((returnval[i]/len(s)))
    dS = dS*-1
    return dS

#usefullness is basically what uses the entropy and gets the value on how viable it is.
# ie. if it is zero then it is useless

def usefullness(trait, s):
    potential_candidates = {}
    dS = 0
    for i in s:
        if i[trait] in potential_candidates: potential_candidates[i[trait]].append(i)
        else: potential_candidates[i[trait]] = [i]
    for i in potential_candidates: dS += (len(potential_candidates[i])/len(s)) * delta_s(potential_candidates[i], groups)
    return delta_s(s, groups) - dS


#building logically, just like we did in class
#took a while to figure out how to do with dictionaries
#had to sit down and draw it out
def build(tree, s, g):
    best_trait = ''
    useful = 0
    print(type(g))
    input()
    temp = g[:len(g) - 1]
    for i in temp:
        counter = usefullness(i, s)
        if counter > useful:
            useful = counter
            best_trait = i
    tree[best_trait] = {}
    #making a node

    potential_candidates = {}
    for i in s:
        if i[best_trait] in potential_candidates: potential_candidates[i[best_trait]].append(i)
        else: potential_candidates[i[best_trait]] = [i]
    for value in potential_candidates:
        tree[best_trait][value] = {}
        #tree of tree

        #if entropy is not useless, then recur
        #otherwise, just build the tree and leave it there
        if delta_s(potential_candidates[value], g) != 0: build(tree[best_trait][value], potential_candidates[value], g)
        else: tree[best_trait][value] = potential_candidates[value][0][g[len(g) - 1]]

    return tree


def output(tree, s, g, temp):
    for key, value in tree.items():
        f.write(" - " * temp + "" + str(key))
        if type(value) != dict: f.write(" -----> " + str(value +  "\n"))
        else:
            f.write("\n")
            #recur
            output(value, s, g, temp + 1)

groups = []
store = []

with open(sys.argv[1]) as f:
    templine = []
    for line in f:
        line = line.strip().upper()
        items = line.split(",")
        templine.append(items)

    # groups = templine[0]
    # store = [{groups[i]: templine[j][i]} for j in range(1, len(templine)) for i in range(len(groups))]

    for j in range(len(templine)):
        groups = templine[0]
        if j > 0:
            temp = {}
            for i in range(len(groups)): temp[groups[i]] = templine[j][i]
            store.append(temp)

return_tree = {}
#need a normal one to enter recursion

return_tree = build(return_tree, store, groups)
print(return_tree)
input()
#w+ means read and write
with open("treeout.txt", "w+") as f:
    output(return_tree, store, groups, 0)
    f.seek(0)
    file_contents = f.read()
