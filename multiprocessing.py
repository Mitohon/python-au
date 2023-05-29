import multiprocess as mp
from multiprocess import Pool
import time
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

def main():
    n = 1000
    a = []
    start_p = time.time()
    with Pool(4) as p:
        a = p.map(MonteCarlo, [n] * n)

    end_p = time.time()
    print(
        'примерное значение интеграла',
        sum(a) / n,
        'потребовалось времени c мультипроцессингом',
        end_p - start_p)
    a = []
    start = time.time()
    for i in range(n):
        a.append(MonteCarlo(n))
    end = time.time()
    print(
        'примерное значение интеграла',
        sum(a) / n,
        'потребовалось времени без мультипроцессинга',
        end - start)


if __name__ == "__main__":
    main()
