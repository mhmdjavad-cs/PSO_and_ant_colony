import random
import numpy as np
import math
#from numba import jit
import time


# constants :
DIMENSION = 229
alpha = 2
beta = 2
Q = 10
evaporation = 0.9
file_name = "gr229"
BEST_VAL = 200
ELITE = 1400
SUPER_ELITE = 1200
found = 1000

def get_distance_matrix(n):
    tsp_data = open(f"{file_name}.txt", "r")
    tsp_data = tsp_data.readlines()
    lines = []

    for line in tsp_data:
        data = [line.split(" ")[1],line.split(" ")[2]]
        #print(data)
        lines.append(data)

    for data in lines:
        data[1] = data[1][:-1]

    distance = np.zeros((n,n))
    for i in range(0,n):
        for j in range(0,n):
            #print(i," ",j)
            distance[i][j] = round(math.sqrt((float(lines[i][0]) - float(lines[j][0]))**2 + (float(lines[i][1]) - float(lines[j][1]))**2) , 2)

    return distance

def initial_pheromone():
    pheromone_matrix = np.ones((DIMENSION,DIMENSION))
    return  pheromone_matrix

def list_of_cities():
    feasible_cities = [i for i in range(2, DIMENSION + 1)]
    return feasible_cities

def get_value(distance_matrix):
    value = np.zeros((DIMENSION,DIMENSION))
    for i in range(0,DIMENSION):
        for j in range(0,DIMENSION):
            if(i != j):
                value[i][j] = round(BEST_VAL/distance_matrix[i][j], 2)
    return value


def select(value,pheromone,feasible,current):
    sum = 0
    for node in feasible:
        sum += ((pheromone[current-1][node-1])**alpha)*((value[current-1][node-1])**beta)

    probability = []
    for node in feasible:
        probability.append( (((pheromone[current-1][node-1])**alpha)*((value[current-1][node-1])**beta))/sum  )
    #print("probability: ", probability)

    action = np.random.choice(feasible,size=1,p=probability)
    return action[0]

def cost_function(answer,distance_matrix):
    cost = 0
    for i in range(0,DIMENSION-1):
        cost += distance_matrix[answer[i]-1][answer[i+1]-1]
    cost += distance_matrix[answer[0]-1][answer[-1]-1]
    return cost

def pheromone_update(pheromone,ant,value,cost):
    for i in range(0,DIMENSION):
        pheromone[i] = evaporation * pheromone[i]

    if cost <= SUPER_ELITE:
        for i in range(0, DIMENSION - 1):
            pheromone[ant[i]-1][ant[i+1]-1] = 50 * Q * value[ant[i]-1][ant[i+1]-1]
            pheromone[ant[i+1] - 1][ant[i] - 1] = 50 * Q * value[ant[i+1] - 1][ant[i] - 1]
        pheromone[ant[0] - 1][ant[-1] - 1] = 50 * Q * value[ant[0] - 1][ant[-1] - 1]
        pheromone[ant[-1] - 1][ant[0] - 1] = 50 * Q * value[ant[-1] - 1][ant[0] - 1]
    elif cost <= ELITE:
        for i in range(0, DIMENSION - 1):
            pheromone[ant[i]-1][ant[i+1]-1] = 30 * Q * value[ant[i]-1][ant[i+1]-1]
            pheromone[ant[i+1] - 1][ant[i] - 1] = 30 * Q * value[ant[i+1] - 1][ant[i] - 1]
        pheromone[ant[0] - 1][ant[-1] - 1] = 30 * Q * value[ant[0] - 1][ant[-1] - 1]
        pheromone[ant[-1] - 1][ant[0] - 1] = 30 * Q * value[ant[-1] - 1][ant[0] - 1]
    else:
        for i in range(0, DIMENSION-1):
            pheromone[ant[i]-1][ant[i+1]-1] = Q * value[ant[i]-1][ant[i+1]-1]
            pheromone[ant[i+1] - 1][ant[i] - 1] = Q * value[ant[i+1] - 1][ant[i] - 1]
        pheromone[ant[0] - 1][ant[-1] - 1] = Q * value[ant[0] - 1][ant[-1] - 1]
        pheromone[ant[-1] - 1][ant[0] - 1] = Q * value[ant[-1] - 1][ant[0] - 1]

    return pheromone

distance = get_distance_matrix(DIMENSION)
value = get_value(distance)
print(distance)
print(value)
pheromone = initial_pheromone()
print(pheromone)

for t in range(0,10000):
    ant = []
    feasible = list_of_cities()
    ant.append(1)
    for k in range(0, DIMENSION-1):
        action = select(value,pheromone,feasible,ant[-1])
        #print("action is:", action)
        feasible.remove(action)
        ant.append(action)
        #print(k,"- ant is: ", ant)
        #print("remaining: ", feasible)

    cost = cost_function(ant,distance)
    print(cost)
    pheromone = pheromone_update(pheromone,ant,value,cost)
    #print(pheromone)
    if cost <= found:
        break

for row in pheromone:
    for item in row:
        if item <= 1:
            print(0," ",end=" ")
        else:
            print(round(item,1),end=" ")
    print()

print(ant)
print(cost)