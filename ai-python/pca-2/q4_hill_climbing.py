"""
Question 4: Hill Climbing Algorithm to Maximize f(x) = -x^2 + 5x + 10.
Matches lab style with per-iteration progress and final best solution output.
"""

import random


# Define the objective function (the function we want to maximize)
def objective_function(x):
    return -(x ** 2) + 5 * x + 10


# Hill climbing algorithm
def hill_climbing(starting_point, step_size=0.1, max_iterations=200):
    current_solution = starting_point
    current_value = objective_function(current_solution)

    for i in range(max_iterations):
        # Generate a neighboring solution
        next_solution = current_solution + random.uniform(-step_size, step_size)
        next_value = objective_function(next_solution)

        # If the new solution is better, move to the new solution
        if next_value > current_value:
            current_solution = next_solution
            current_value = next_value
            print(f"Iteration {i}: Current best solution is {current_solution} with value {current_value}")

    return current_solution, current_value


random.seed(42)
starting_point = random.uniform(-10, 10)
print(f"Initial random starting point: {starting_point} with value {objective_function(starting_point)}")

best_solution, best_value = hill_climbing(starting_point)
print(f"\nBest solution found: {best_solution} with value {best_value}")
