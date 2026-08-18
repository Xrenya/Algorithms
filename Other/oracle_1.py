from collections import deque

"""

A = [1, 3, -1, 5, 3, 6]
x = 3

Windows:
[1, 3, -1]  -> min = -1
[3, -1, 5]  -> min = -1
[-1, 5, 3]  -> min = -1
[5, 3, 6]   -> min = 3

Answer = 3
"""
A = [1, 3, -1, 5, 3, 6]
x = 3

def func(array, x):
    q = deque([])
    for i in range(x):
        while q and array[q[-1]] > array[i]:
            q.pop()
        q.append(i)
    output = []
    output.append(array[q[0]])
    for i in range(x, len(array)):
        if q[0] + x == i:
            q.popleft()
            
        while q and array[q[-1]] > array[i]:
            q.pop()
        q.append(i)
        output.append(array[q[0]])
    
    return max(output)
    
print(func(A, x))
