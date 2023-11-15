# find the solution of the equation
import random

lr = 0.001

def function(x):
	return x**2 - 5*x + 4

def grad(x):
  return 2*x - 5


cur_x = random.randint(-5, 5)
eps = 0.001


while True:
  y_pred = function(cur_x)
  #print(cur_x, y_pred)
  if abs(y_pred) <= eps:
    break
  grad_val = grad(cur_x)
  if grad_val > 0:
    if y_pred > 0:
      cur_x -= lr #* grad_val
    else:
      cur_x += lr
  else:
    if y_pred > 0:
      cur_x += lr #* grad_val
    else:
      cur_x -= lr
