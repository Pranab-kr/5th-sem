import random

def objective_function(x):
    return -(x**2) + 5*x + 10

def hill_climbing(starting_point, step_size=0.1, max_iterations=100):
    current_solution = starting_point
    current_value = objective_function(current_solution)
    
    for i in range(max_iterations):
        next_solution = current_solution + random.uniform(-step_size, step_size)
        next_value = objective_function(next_solution)
        
        if next_value > current_value:
            current_solution = next_solution
            current_value = next_value
            print(f"Iteration {i}: Current best solution is {current_solution} with value {current_value}")
            
    return current_solution, current_value

starting_point = random.uniform(-10, 10)
best_solution, best_value = hill_climbing(starting_point)
print(f"\nBest solution found: {best_solution} with value {best_value}")