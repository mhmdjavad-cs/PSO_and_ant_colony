import random
import numpy as np
import math
#from numba import jit
import time


# constants :
DIMENSION = 1002
alpha = 1.2
beta = 1
Q = 7
evaporation = 0.8
file_name = "gr229"
BEST_VAL = 100000
ELITE = 900000
SUPER_ELITE = 800000
found = 700000

def get_distance_matrix(n):
    tsp_data = open(f"{file_name}.txt", "r")
    tsp_data = tsp_data.readlines()
    lines = []

    for line \
            in tsp_data:
        data = [line.split(" ")[3]]
        #print(data)
        lines.append(data)

    print(lines)
    for i in range(0,len(lines)):
        lines[i] = float(lines[i][0])

    print(lines)

    for data in lines:
        data[1] = data[1][:-1]

    distance = np.zeros((n,n))
    for i in range(0,n):
        for j in range(0,n):
            #print(i," ",j)
            distance[i][j] = round(math.sqrt((float(lines[i][0]) - float(lines[j][0]))**2 + (float(lines[i][1]) - float(lines[j][1]))**2) , 2)

    return distance

get_distance_matrix(229)