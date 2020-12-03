import numpy as np
rows, cols = [int(x) for x in input().split()]
matrix = np.ones([rows, cols])
def pascal(matrix):
    for row in range(1, rows):
        for col in range(1, cols):
            matrix[row, col] = matrix[row-1, col] + matrix[row, col-1]
    return matrix

pascal(matrix)
