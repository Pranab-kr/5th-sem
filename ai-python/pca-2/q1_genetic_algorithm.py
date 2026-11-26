import numpy as np
from geneticalgorithm import geneticalgorithm as ga

# (a) Maximize sum of sine values of a real-valued vector X in [0, 10]
def f1(X):
    return -np.sum(np.sin(X))

varbound1 = np.array([[0, 10]] * 3)
model1 = ga(function=f1, dimension=3, variable_type='real', variable_boundaries=varbound1)
model1.run()

# (b) Maximize sum of three integer decision variables in [0, 10]
def f2(X):
    return -np.sum(X)

varbound2 = np.array([[0, 10]] * 3)
model2 = ga(function=f2, dimension=3, variable_type='int', variable_boundaries=varbound2)
model2.run()

# (c) Maximize sum of 30 Boolean decision variables
def f3(X):
    return -np.sum(X)

model3 = ga(function=f3, dimension=30, variable_type='bool')
model3.run()
