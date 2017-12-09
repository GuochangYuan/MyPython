import numpy as np
import math

from scipy.linalg import solve

a = np.array([[9, 53, 381], [53, 381, 3017], [381, 3017, 25317]])
b = np.array([32, 147, 1025])
x = solve(a, b)
print(x)
print(math.sin(pi/2))


