import numpy as np
from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box
from numpy import vectorize
from operator import add


def multiply(x, a):
    return x * a

def vect_mult():
    return vectorize(multiply)

def gauss(a, b):
    ab = np.concatenate((a, np.array([b]).T), axis=1) # concatenate заодно и скопирует 
    d = len(ab)  # размер по старшему измерению
    for i in range(d):
        j = i
        while j < len(a[i]) and ab[i][j] == 0:
            j += 1
        if j == len(a[i]):
            continue
        r = vectorize(multiply)
        ab[i] = r (ab[i], 1/ab[i][j])
        for k in range(i+1, d):
            ab[k] = ab[k] - ab[k][j]*ab[i]
       
    #проверка на совместимость 
    for i in range(d):            
        nonzero_r = False
        for j in range(len(a[i])):
            if abs(ab[i][j]) > 10**(-10):
                nonzero_r = True
        if nonzero_r == False and abs(ab[i][-1]) > 10**(-10):
            return 'решений нет'
    
    solution = [0]*len(ab)
    for i in range(len(ab)-1, -1, -1):
        res = ab[i][-1]
        for j in range(len(ab[i])-2, i-1, -1):
            res -= ab[i][j]*solution[j]
        if ab[i][i] != 0:
            solution[i] = res / ab[i][i]
    return solution


a = np.array([
    [0, 2, 1, 3],
    [1, 1, 1, 1],
    [0, 4, 5, 7],
    [2, 2, 2, 2]
], dtype=float)

b = np.array([5, 6, 7, 12], dtype=float)

print(np.concatenate((a, np.array([b]).T), axis=1))
print("\nРешения системы:")
print(gauss(a,b))
