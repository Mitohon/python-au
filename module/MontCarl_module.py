import random
from math import cos, pi  # интеграл cos(x) на отрезке [-pi/2; pi/2]
import MonteCarlo
MonteCarlo.MonteCarlo(100)
N = 1000  # тест
for n in range(100, N, 100):
    MC = MonteCarlo.MonteCarlo(n)
    print("n =", n, " ", MC, "\t", abs(MC - 2))
