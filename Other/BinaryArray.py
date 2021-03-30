from math import log, floor

def solution(A):
  array = []
  acc = 0
  for i in A:
    acc = acc + 2 ** i
  while acc != 0:
    power = floor(log(acc, 2))
    array.append(power)
    acc = acc - 2 ** power
  print(array)
  
solution([2,3,0])
