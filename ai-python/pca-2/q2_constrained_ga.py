import numpy as np
from geneticalgorithm import geneticalgorithm as ga

# (a) Objective function with penalty term for constraint X[0] + X[1] >= 2
def f(X):
    pen = 0
    if X[0] + X[1] < 2:
        pen = 500 + 1000 * (2 - X[0] - X[1])
    return np.sum(X) + pen

# (b) & (c) Configure, execute GA, and display best solution & objective value
varbound = np.array([[0, 10]] * 3)
model = ga(function=f, dimension=3, variable_type='real', variable_boundaries=varbound)
model.run()
