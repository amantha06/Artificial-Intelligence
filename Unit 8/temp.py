import sys
import math
import random
import matplotlib.pyplot as pyplt


def main():
    file = open(sys.argv[1], "r")
    feat_list = sort_csv(file.readline())
    nonmissing = {feat: [] for feat in feat_list}
    total = 0
    for line in file:
        parsed_line = sort_csv(line)
        for i, feat in enumerate(feat_list):
            nonmissing[feat].append(parsed_line[i])
        total += 1

    train_data, test_data = separate_train_test(int(sys.argv[2]), nonmissing, total)
    accuracies = []

    for size in range(int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])):
        temp_train = set()
        temp_train.add(random.randint(0, total - int(sys.argv[2]) - 1))
        outcome = train_data[feat_list[-1]][list(temp_train)[0]]

        while len(temp_train) != 2:
            temp = random.randint(0, total - int(sys.argv[2]) - 1)
            if train_data[feat_list[-1]][temp] != outcome:
                temp_train.add(temp)

        while len(temp_train) != size:
            temp_train.add(random.randint(0, total - int(sys.argv[2]) - 1))

        attrs = {feat: [train_data[feat][idx] for idx in temp_train] for feat in feat_list}
        decision_tree = {}
        build_optimal_tree(0, decision_tree, '', feat_list, attrs)
        accuracy = 0

        for i in range(int(sys.argv[2])):
            branch = decision_tree
            while type(branch) != str:
                key = list(branch.keys())[0]
                outcome = test_data[key][i]
                if outcome not in branch[key].keys():
                    branch = random.choice(list(set(attrs[feat_list[-1]])))
                else:
                    branch = branch[key][outcome]

            if branch == test_data[feat_list[-1]][i]:
                accuracy += 1

        accuracy *= 100 / int(sys.argv[2])
        accuracies.append(accuracy)
        decision_tree = {}

    pyplt.scatter([idx for idx in range(int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))], accuracies)
    pyplt.xlabel("Training Set Size")
    pyplt.ylabel("Accuracy")
    pyplt.show()


def build_optimal_tree(depth, tree_branch, current, feat_list, data):
    entropies = [find_entropy(i, feat_list, data) for i in range(0, len(feat_list) - 1)]

    if max(entropies) == min(entropies) and max(entropies) != 0.0:
        tree_branch[current] = random.choice(list(set(data[feat_list[-1]])))
        return

    next_feat = feat_list[entropies.index(min(entropies))] if max(entropies) != 0.0 else ''

    if next_feat != '' and min(entropies) != 0.0:
        if depth != 0:
            tree_branch[current] = {next_feat: {}}
            tree_branch = tree_branch[current]
            current = next_feat
            depth += 1
        else:
            current = next_feat

        tree_branch[current] = {feat: {} for feat in set(data[next_feat])}

    elif next_feat != '':
        if depth != 0:
            tree_branch[current] = {next_feat: {feat: '' for feat in set(data[next_feat])}}
            for val in set(data[next_feat]):
                tree_branch[current][next_feat][val] = data[feat_list[-1]][data[next_feat].index(val)]
        else:
            tree_branch[next_feat] = {feat: '' for feat in set(data[next_feat])}
            for val in set(data[next_feat]):
                tree_branch[next_feat][val] = data[feat_list[-1]][data[next_feat].index(val)]
    else:
        tree_branch[current] = data[feat_list[-1]][0]
    if min(entropies) == 0.0:
        return

    unique_values = set(data[next_feat])
    for val in unique_values:
        new_feats, new_data = create_new_split(feat_list, next_feat, val, data)
        build_optimal_tree(depth + 1, tree_branch[current], val, new_feats, new_data)

def sort_csv(line):
    parsed_line = line.split(',')
    if parsed_line[-1][-1] == '\n':
        parsed_line[-1] = parsed_line[-1][:-1]
    return parsed_line


def separate_train_test(n, attributes, global_total):
    indices = [i for i in range(global_total)]
    random.shuffle(indices)
    train = {key: [attributes[key][i] for i in indices[:-n]] for key in attributes.keys()}
    test = {key: [attributes[key][i] for i in indices[-n:]] for key in attributes.keys()}
    return train, test


def find_entropy(index, feat_list, data):
    values = set(data[feat_list[index]])
    entropy = 0

    for value in values:
        indices = [outcome for i, outcome in enumerate(data[feat_list[-1]]) if data[feat_list[index]][i] == value]
        outcomes = list(set(indices))

        if index != len(feat_list) - 1:
            temp_entropy = 0
            for outcome in outcomes:
                if indices.count(outcome) != 0:
                    temp_entropy += (indices.count(outcome) / len(indices)) * math.log(indices.count(outcome) / len(indices), 2)
        else:
            temp_entropy = math.log(len(indices) / len(data[feat_list[-1]]), 2)

        entropy -= (len(indices) / len(data[feat_list[-1]])) * temp_entropy

    return entropy


def create_new_split(feat_list, feat_index, feat_type, data):
    selected_indices = [i for i in range(len(data[feat_index])) if data[feat_index][i] == feat_type]
    updated_feats = [feat for feat in feat_list if feat != feat_index]
    updated_data = {}
    for feat in feat_list:
        if feat != feat_index:
            updated_data[feat] = [data[feat][i] for i in selected_indices]

    return updated_feats, updated_data


if __name__ == "__main__":
    main()