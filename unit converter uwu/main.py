import numpy as np

# mass, length, time, electrical current
TARGET = np.array([0,1,0,0])
MIN = -1
MAX = 1

Hz = np.array([0,0,-1,0])
N = np.array([1,1,-2,0])
Pa = np.array([1,-1,-2,0])
J = np.array([1,2,-2,0])
W = np.array([1,2,-3,0])
C = np.array([0,0,1,1])
V = np.array([1,2,-3,-1])
Ohm = np.array([1,2,-3,-2])
F = np.array([-1,-2,4,2])
T = np.array([1,0,-2,-1])

units = np.array([Hz, N, Pa, J, W, C, V, Ohm, F, T])

while True:
    coefs = np.random.randint(MIN, MAX+1, units.shape[0])
    if np.all(np.dot(coefs, units) == TARGET) and 0 not in coefs:
        print(coefs)
        break