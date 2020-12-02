import numpy as np
rows = int(input())
matrix = np.empty([rows, rows])
def equal(matrix):
    for row in range(rows):
        matrix[row] = np.array([int(x) for x in input().split()])
    for i in range(1, rows):
        if (matrix[i:, i-1] != matrix[i-1, i:]).any():
            return "NO"
    return "YES"
equal(matrix)
