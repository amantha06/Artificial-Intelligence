import sys

zero = 0
one = 1
two = 2

def excecute(test):
    state = zero
    for index in test:
        if index not in dfa[state]: return False
        state = dfa[state][index]
    return state in returnval
#not doing anything lol

catalyst_int = None
try:
    catalyst_int = zero; input_list = int(sys.argv[1])
except:
    catalyst_int = one

if catalyst_int == one:
    with open(sys.argv[one]) as file: problem_number_list = [i.strip() for i in file]
    returnval, templist, tempnum = [int(i) for i in problem_number_list[2].split(" ")], problem_number_list[0], int(problem_number_list[1])

with open(sys.argv[2]) as file: mainlisttwo = [i.strip() for i in file]

dfa = {
0: {
"b": 1
},
1: {
"a": 1,
"b": 2
},
2: {}
}
final = [1, 2]


#languages
one = {0: {"a": 1, "b": 4}, 1: {"a": 2, "b": 4}, 2: {"a": 4, "b": 3}, 3: {"a": 4, "b": 4}, 4: {"a": 4, "b": 4}}
two = {0: {"0": 0, "1": 1, "2": 0}, 1: {"0": 0, "1": 1, "2": 0}}
three = {0: {"a": 0, "b": 1, "c": 0}, 1: {"a": 1, "b": 1, "c": 1}}
four = {0: {"0": 1, "1": 0}, 1: {"0": 0, "1": 1}}
five = {0: {"0": 1, "1": 2}, 1: {"0": 0, "1": 3}, 2: {"0": 3, "1": 0}, 3: {"0": 2, "1": 1}}
six = {0: {"a": 1, "b": 0, "c": 0}, 1: {"a": 1, "b": 2, "c": 0}, 2: {"a": 1, "b": 0, "c": 3}, 3: {"a": 3, "b": 3, "c": 3}}
seven = {0: {"0": 0, "1": 1}, 1: {"0": 2, "1": 1}, 2: {"0": 2, "1": 3}, 3: {"0": 2, "1": 4}, 4: {"0": 4, "1": 4}}

predetermined_list_of_everything = [[(("a", "b")), (("0", "1")), (("a", "b")), (("0", "1")), (("0", "1")), (("a", "b", "c")), (("0", "1"))],[3, 1, 1, 0, 0, (0, 1, 2), 4],[one, two, three, four, five, six, seven]]

if catalyst_int == 1:
    dfa, temp_dict = {}, {}
    iterator, temp = zero, zero
    problem_number_iter = iter(problem_number_list)
    i = next(problem_number_iter, None)
    while i is not None:
        if iterator > 4:
            if len(i) == 1:
                dfa[temp] = temp_dict.copy()
                temp, temp_dict = int(i), {}
            elif len(i) != 0:
                char, to_state = i.split(" ")
                temp_dict[char] = int(to_state)
        if iterator == 4: temp = int(i)
        iterator += 1
        i = next(problem_number_iter, None)
    dfa[temp] = temp_dict

else:
    dfa = predetermined_list_of_everything[2][input_list - 1]
    returnval = []
    if input_list == 6:
        for i in predetermined_list_of_everything[1][input_list - 1]:
            returnval.append(i)
    else:
        returnval.append(predetermined_list_of_everything[1][input_list - 1])
#possible to do with walrus operator, but not able to figrue it out
def get_main_value(inp):
    i, j = zero, zero
    for i in range(len(inp)):
        temp, dfaval = inp[i], dfa[j]
        if temp not in dfaval:
            return False
        j = dfaval[temp]
    if j in returnval:
        return True
    return False


printing_val = "*"
try: templist
except: templist = [x for x in predetermined_list_of_everything[0][input_list - 1]]
for i in templist: printing_val += "\t" + i
print(printing_val)
for i in dfa:
    final_str = str(i) + "\t" + "\t".join(str(dfa[i].get(j, "__")) for j in templist)
    print(final_str)
print("final nodes:", returnval)
for line in mainlisttwo: print(get_main_value(line), line)
