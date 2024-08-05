import sys
import math
import random
import matplotlib.pyplot as pyplt
#has a bunch of rnadom if statements that I used for debugging, and no need to take away
#helped a lot

def delta_s(ind, g, att):
    zero = 0
    d_s = zero
    v_i = set(att[g[ind]])

    for i_v in v_i:
        ind2 = []
        for i, k in enumerate(att[g[-1]]):
            if att[g[ind]][i] == i_v:
                ind2.append(k)

        #remove overlap
        k_s = list(set(ind2))

        t_s = sum((ind2.count(i) / len(ind2)) * math.log(ind2.count(i) / len(ind2), 2) for i in k_s if
                  ind2.count(i) != zero) if ind != len(g) - 1 else math.log(len(ind2) / len(att[g[-1]]), 2); d_s -= (len(ind2) / len(att[g[-1]])) * t_s

    return d_s

# def delta_s(ind, g, att):
#     t_i = len(att[g[-1]])
#     d_s = 0
#
#     v_i = iter(set(att[g[ind]]))
#     check = next(v_i, None)
#
#     while check is not None:
#         v_i2 = [i for i, j in enumerate(att[g[-1]]) if att[g[ind]][i] == check]
#         u_o = set(v_i2)
#         v_i3 = len(v_i2)
#
#         if ind != len(g) - 1:
#             t_s = 0
#             for o in u_o:
#                 o_c = v_i2.count(o)
#                 if o_c != 0:
#                     t_s += (o_c / v_i3) * math.log((o_c / v_i3), 2)
#         else:
#             t_s = math.log(v_i3 / t_i, 2)
#
#         d_s -= (v_i3 / t_i) * t_s
#
#         check = next(v_i, None)
#
#     return d_s

#FIX THESE METHDS
def build(d, branch, temo, group, info):
    d_s = []
    for i in range(zero, len(group) - 1):
        result = delta_s(i, group, info)
        d_s.append(result)

    min_s = min(d_s)
    max_s = max(d_s)
    zeropointzero = 0.0

    if max_s == min_s:
        if max_s != zeropointzero:
            if 2 == 2:
                branch[temo] = random.choice(list(set(info[group[-1]])))
                return


    if max_s != zeropointzero:
        min_index = d_s.index(min_s)
        new_t = group[min_index]
    elif not max_s != zeropointzero:
        new_t = ''



    if new_t != '' and min_s != zeropointzero and 1 == 1:
        if d != zero:
            branch[temo] = {new_t: {}}; branch = branch[temo]; temo = new_t; d += 1
        elif not d != zero:
            temo = new_t

        branch[temo] = {}
        for jk in set(info[new_t]):
            branch[temo][jk] = {}

    elif zeropointzero == zeropointzero and new_t != '':
        if d != zero:
            branch[temo] = {new_t: {i: '' for i in set(info[new_t])}}

            for val in set(info[new_t]): branch[temo][new_t][val] = info[group[-1]][info[new_t].index(val)]

        elif not d != zero:
            branch[new_t] = {}
            for i in set(info[new_t]): branch[new_t][i] = ''

            for i in set(info[new_t]): branch[new_t][i] = info[group[-1]][info[new_t].index(i)]
    else: branch[temo] = info[group[-1]][0]


    if min_s == zeropointzero:
        if min_s == min_s:
            return

    unique_values = set(info[new_t])
    val_iterator = iter(unique_values)
    while True:
        try:
            val = next(val_iterator)
            #temp method just makes life sm easier
            new_feats, new_data = temp_method(group, new_t, val, info)
            build(d + one, branch[temo], val, new_feats, new_data)
        except StopIteration:
            break


def temp_method(f_list, ind, typ, info):
    if zero == zero:
        news = 0.12345

    s_i = []
    for i in range(len(info[ind])):
        if info[ind][i] == typ:
            s_i.append(i)

    u_f = []
    for i in f_list:
        if i != ind:
            u_f.append(i)

    if zero == zero:
        news = 0.12345

    u_d = {}
    for feat in f_list:
        if feat != ind:
            if 2 == 2:
                u_d[feat] = []
                for i in s_i:
                    u_d[feat].append(info[feat][i])

    return u_f, u_d



zero, one, two = 0, 1, 2

inp1, inp2, inp3, inp4, inp5 = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])

file = open(inp1, "r")
temp = file.readline().split(',')
if temp[-1][-1] == '\n': temp[-one] = temp[-one][:-one]

checkdict = {}
for i in temp:
    checkdict[i] = []

count = zero
for i in file:
    organize = i.split(',')
    if organize[len(organize) - one][-one] == '\n': organize[len(organize) - one] = organize[len(organize) - one][:-one]

    for j, k in enumerate(temp):
        checkdict[k].append(organize[j])
    count+=one


training_testing_index = []
for i in range(count):
    training_testing_index.append(i)
random.shuffle(training_testing_index)

train = {}
for k in checkdict.keys():
    train[k] = [checkdict[k][i] for i in training_testing_index[:-inp2]]
test = {}
for k in checkdict.keys():
    test[k] = [checkdict[k][i] for i in training_testing_index[-inp2:]]


acc = []
for s in range(inp3, inp4, inp5):
    t_train = set()
    t_train.add(random.randint(zero, count - inp2 - one))
    returnval = train[temp[-1]][list(t_train)[0]]

    while len(t_train) != two:
        temp2 = random.randint(zero, count - inp2 - one)
        if train[temp[-one]][temp2] != returnval: t_train.add(temp2)

    while len(t_train) != s:
        t_train.add(random.randint(zero, count - inp2 - one))

    attribute_dict = {i: [train[i][j] for j in t_train] for i in temp}

    final_tree = {}

    build(zero, final_tree, '', temp, attribute_dict)
    accu = zero

    for i in range(inp2):
        b = final_tree
        while type(b) != str:
            key = list(b.keys())[0]
            returnval = test[key][i]
            b = random.choice(list(set(attribute_dict[temp[-1]]))) if returnval not in b[key].keys() else b[key][
                returnval]

        if b == test[temp[-1]][i]: accu += one

    accu *= 100 / inp2
    acc.append(accu)
    final_tree = {}
    print(accu)


x_values = []
for i in range(inp3, inp4, inp5):
    x_values.append(i)
pyplt.scatter(x_values, acc)
pyplt.xlabel("Training Set Size")
pyplt.ylabel("Accuracy")
pyplt.show()