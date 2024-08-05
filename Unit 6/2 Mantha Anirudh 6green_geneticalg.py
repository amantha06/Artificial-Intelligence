import sys
import math
import random

#alphabet = "ETAOINSRHLDCUMFPGWYBVKXJQZ"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

POPULATION_SIZE = 500
NUM_CLONES = 1
TOURNAMENT_SIZE = 20
TOURNAMENT_WIN_PROBABILITY = .75
CROSSOVER_LOCATIONS = 5
MUTATION_RATE = .8

file1 = sys.argv[1]
n_grams_store = {}
with open("ngrams.txt") as f1:
    for line in f1:
        line = line.strip().split()
        n_grams_store[line[0]] = float(line[1])

def decode(message, translator):
    returnval = ""
    for i in message.upper():
        if i not in translator: returnval += i
        else: returnval += alphabet[translator.index(i)]
    return returnval

def encode(message, translator):
    returnval = ""
    for i in message.upper():
        if i not in alphabet: returnval += i
        else: returnval += translator[alphabet.index(i)]
    return returnval



def fitness(n_value, message, translator):
    zero = 0
    two = 2
    one = 1
    n_grams = []
    message, sum = decode(message, translator), zero
    for i in range(len(message) - n_value + one): n_grams.append(message[i:(i+n_value)])
    for n in n_grams:
        if n in n_grams_store: sum += math.log(n_grams_store[n], two)
    return sum

def genetic(message):
    population = set()
    translator = alphabet
    while(len(population) != POPULATION_SIZE):
        temp = random.sample(translator, 2)
        start, finish = sorted([translator.index(temp[0]), translator.index(temp[1])])
        translator = translator[:start] + translator[finish] + translator[start+1:finish] + translator[start] + translator[finish+1:]
        population.add(translator)

    count = 0
    while count <= 500:
        if count > 0: population = next_gen.copy()
        fitness_score = {}
        for i in population: fitness_score[i] = fitness(3, message, i)
        fitness_ranking = sorted(fitness_score.items(), key=lambda x:x[1])
        next_gen = set()
        for i in range(1, NUM_CLONES+1): next_gen.add(fitness_ranking[-i][0])
        if count % 1 == 0:
            print(decode(message, fitness_ranking[-1][0]))
            print()

        tournament_random = random.sample(list(population), TOURNAMENT_SIZE*2)
        tournament1, tournament2 = {}, {}
        for i in range(len(tournament_random)):
            if i % 2 == 0: tournament1[tournament_random[i]] = fitness_score[tournament_random[1]]
            else: tournament2[tournament_random[i]] = fitness_score[tournament_random[i]]

        tournament1, tournament2 = sorted(tournament1.items(), key = lambda  x:x[1]), sorted(tournament2.items(), key = lambda  x:x[1])

        while len(next_gen) <= POPULATION_SIZE:
            temp1, temp2 = None, None
            for i in range(len(tournament1)):
                if random.random() < TOURNAMENT_WIN_PROBABILITY:
                    temp1 = tournament1[-i][0]
                    break
            for i in range(len(tournament2)):
                if random.randint(0, 1) < TOURNAMENT_WIN_PROBABILITY:
                    temp2 = tournament2[-i][0]
                    break
            if temp1 == None: temp1 = tournament1[-1][0]
            if temp2 == None: temp2 = tournament2[-1][0]

            if fitness_score[temp1] > fitness_score[temp2]: primary, secondary = temp1, temp2
            else: primary, secondary = temp2, temp1

            phs = []
            for i in phs:
                index = secondary.index(i)
                phs.append(index)
            phs = sorted(phs)
            generations = ["."]*(13+13)
            for i in phs:
                generations[i], primary = secondary[i], primary.replace(secondary[i], "")
                primary = primary.replace(secondary[i], "")
            for i in range(len(generations)):
                if generations[i] == ".":
                    generations[i], primary = primary[0], primary[1:]
            final = "".join(generations)

            if random.randint(0,1) < MUTATION_RATE:
                temp = random.sample(final, 2)
                start, end = sorted([final.index(temp[0]), final.index(temp[1])])
                final = final[:start] + final[end] + final[start+1:end] + final[start] + final[end+1:]
            next_gen.add(final)
        count+=1

one = 1
yes = sys.argv[one]
genetic(yes)






