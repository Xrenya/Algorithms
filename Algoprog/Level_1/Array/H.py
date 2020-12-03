import numpy as np

rows, cols = [int(x) for x in input().split()]
matrix = np.empty([rows, cols])
def find_max(matrix):
    for row in range(matrix.shape[0]):
        matrix[row] = np.array([int(x) for x in input().split()])
    return matrix.max(), np.where(matrix == matrix.max())
    
find_max(matrix)

def find_max_1(matrix):
    for row in range(matrix.shape[0]):
        matrix[row] = np.array([int(x) for x in input().split()])
    maximum = -float("inf")
    coordinates = ()
    for row, row_array in enumerate(matrix):
        for col, element in enumerate(row_array):
            if element > maximum:
                maximum = element
                coordinates = (row, col)
    return maximum, coordinates

find_max_1(matrix)
