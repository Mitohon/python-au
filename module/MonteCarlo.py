import random
from math import cos, pi  # интеграл cos(x) на отрезке [-pi/2; pi/2]
def MonteCarlo(n):
    pi_2 = pi / 2
    point_counter = 0
    for _ in range(n):
        x = random.uniform(-pi_2, pi_2)
        y = random.uniform(0, 1)
        if y <= cos(x):
            point_counter += 1
    return pi * point_counter / n
