import numpy as np
from geneticalgorithm import geneticalgorithm as ga

# (a) Define objective function f(X) = -(X^3 - 3X^2) using NumPy
def f(X):
    return -np.sum(X * X * X - 3 * X * X)

# (b), (c), (d) Configure, run GA, and display best solution & objective value
varbound = np.array([[0, 10]])
model = ga(function=f, dimension=1, variable_type='real', variable_boundaries=varbound)
model.run()
