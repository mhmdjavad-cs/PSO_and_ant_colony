import numpy as np
import random


#cinstants:
file_name = "scp41.txt"
alpha = 1
beta = 1
evaporation = 0.95
base_pheromone = 100
iterations = 1000

def get_data(file_name):
    initial_data = open(f"{file_name}", "r")
    initial_data = initial_data.readlines()

    U, S = int(initial_data[0].split(" ")[1]),int(initial_data[0].split(" ")[2])
    initial_data.pop(0)

    s_costs = []
    count = 0
    for line in initial_data:
        count += 1
        for element in line.split(" "):
            if element == '\n' or element == '':
                continue
            s_costs.append(element)
            if len(s_costs) >= S:
                break
        #initial_data.pop(0)
        if len(s_costs) >= S:
            break

    for i in range(0,count):
        initial_data.pop(0)

    membership = []
    i = 0
    while len(membership) < U:
        #print("len membership: ",len(membership))
        count = int(initial_data[i].split(" ")[1])
        sets = []
        j = i+1
        #print(count ," ", j)
        while len(sets) < count:
            for element in initial_data[j].split(" "):
                if element == "" or element == "\n":
                    continue
                sets.append(int(element))
            j += 1
            i += 1
        i += 1
        membership.append(sets)

    s_costs = list(map(int,s_costs))

    return U,S,s_costs,membership


def select(value,pheromone,feasible,current,ant):
    for node in feasible:
        if node in ant:
            return node

    sum = 0
    for node in feasible:
        sum += ((pheromone[node-1])**alpha)*((1/value[node-1])**beta)

    probability = []
    for node in feasible:
        probability.append( (((pheromone[node-1])**alpha)*((1/value[node-1])**beta))/sum)
    #print("probability: ", probability)

    action = np.random.choice(feasible,size=1,p=probability)
    return action[0]

def correctness_test(number_of_elements,membership,ant):
    for k in range(0, number_of_elements):
        # print(membership[k])
        for subgroup in membership[k]:
            # print("hi ",ant)
            # print(subgroup)
            if subgroup in ant:
                break

            if subgroup == membership[k][-1] and subgroup not in ant:
                print("wrong")


def cost_function(ant,costs):
    sum = 0
    for subset in ant:
        sum += costs[subset-1]
    return sum

def pheromone_update(pheromone, ant, cost):
    value = base_pheromone/cost
    for node in ant:
        pheromone[node-1] += value
    pheromone = list(map(lambda x: x*evaporation, pheromone))

    for i in range(0,len(pheromone)):
        if pheromone[i] < 0.0001:
            pheromone[i] = 0
        else:
            pheromone[i] = round(pheromone[i], 5)

    return pheromone

number_of_elements,number_of_subsets,costs,membership = get_data(file_name)

pheromone = []
for i in range(0,number_of_subsets):
    pheromone.append(1)
best_answer = []
best_cost = 10000

for t in range(0, iterations):
    ant = []
    k = random.randint(0,number_of_elements-1)
    for p in range(0, number_of_elements):
        index = k + p
        index = index%number_of_elements
        feasible = membership[index]
        action = select(costs, pheromone, feasible, index, ant)
        ant.append(action)

    temp_set = set(ant)
    ant = list(temp_set)
    cost = cost_function(ant, costs)
    print("cost: ", cost, " len: ", len(ant))
    if cost < best_cost:
        best_cost = cost
        best_answer = ant[:]
    pheromone = pheromone_update(pheromone, ant, cost)
    print(pheromone)

print("best answer: ", best_answer)
print("number of chosen subsets: ",len(best_answer))
print("best cost: ", best_cost)