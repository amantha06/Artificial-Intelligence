import sys
import math
import random

# • Brown Dwarf -> Star Type = 0
# • Red Dwarf -> Star Type = 1
# • White Dwarf-> Star Type = 2
# • Main Sequence -> Star Type = 3
# • Supergiant -> Star Type = 4
# • Hypergiant -> Star Type = 5

file1 = "star_data.csv"

classification = {}
# with open(file1) as f
#     #https://earthly.dev/blog/csv-python/
#     #specs say another method, but this way seems intuitive
#     dataset = list(csv.reader(f))[1:]
#     for i in range(len(dataset)):
#         classify = dataset[i][4]
#         dataset[i] = dataset[i][:-3]
#         #conditions in specification
#         for j in range(len(dataset[i])): dataset[i][j] = float(dataset[i][j])
#         for j in range(3): dataset[i][j] = math.log(dataset[i][j])
#         temp_tuple = tuple(dataset[i])
#         classification[temp_tuple] = classify
# what was messing me up earlier

with open(file1) as f:
    dataset = [line.split(",") for line in f]
    dataset = dataset[1:]
f_dataset = [(math.log(float(i[0])), math.log(float(i[1])), math.log(float(i[2])), float(i[3]), float(i[4])) for i in
             dataset]


def k_mean_algorithm():
    seven, two, zero, four = 7, 2, 0, 4
    means = random.sample(f_dataset, seven)
    groups = {}
    for i in range(seven): groups[i] = []

    terminator = True
    while terminator:
        for i in range(seven):
            groups[i].clear()  ####################
        for i in f_dataset:
            distance_minimized = 100000000000000000
            mean_minimized = None
            # values reset every data point
            for j in means:
                temp = math.sqrt(sum([(i[k] - j[k]) ** two for k in range(four)]))
                if temp < distance_minimized:
                    distance_minimized = temp
                    mean_minimized = j
            add_index = means.index(mean_minimized)
            groups[means.index(mean_minimized)].append(i)

        terminator = False
        for i in range(seven):
            f_mean = []
            for j in range(four):
                f_mean.append(sum([k[j] for k in groups[i]]) / len(groups[i]))

            if means[i] != f_mean:
                means[i] = f_mean
                terminator = True

    return groups


seven, one, zero = 7, 1, 0
returned_groups = k_mean_algorithm()
for i in range(one, seven + one):
    column_means = []
    print("Group ", i)
    group = returned_groups[i - 1]
    for k in range(len(group[0])):
        column_sum = zero
        for j in range(len(group)): column_sum += group[j][k]
        column_mean = column_sum / len(group)
        column_means.append(column_mean)
    print("Means:", column_means)
    for j in returned_groups[i - 1][::-1]:
        print(j[4])
    print()

# this is cool on whennumber subs work and when they dont.. good observtion