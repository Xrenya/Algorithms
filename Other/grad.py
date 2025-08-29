import random

def function(x):
    return x**2 - 5*x + 4

def grad(x):
    return 2*x - 5
    
lr = 0.001
cur_x = random.randint(-5, 5)
init_x = cur_x
eps = 0.001
max_iterations = 10000
iteration = 0

while iteration < max_iterations:
    y_pred = function(cur_x)
        
    # Gradient descent update
    grad_val = grad(cur_x)
    
    # Check if we've found a solution
    if abs(grad_val) <= eps:
        break
    
    cur_x = cur_x - lr * grad_val  #  Newton's Method
    
    iteration += 1

print(f"Initial value: {init_x}")
print(f"Solution found: x = {cur_x:.6f}")
print(f"Function value at solution: {function(cur_x):.6f}")
print(f"Exact solutions: x = 2.5 y = 2.25")
