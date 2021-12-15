matrix = [[0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 1, 1],
          [0, 0, 0, 1, 1, 1],
          [0, 0, 1, 1, 1, 1],
          [0, 0, 0, 1, 1, 1],
          [0, 0, 0, 0, 1, 1],
          [0, 0, 0, 0, 0, 1]
]
# Find column index of the first one
# Ones start from right to left
# O(MN)
def mat(matrix):
    for index, col in enumerate(zip(*matrix)):
        for num in col:
            if num == 1:
                return index
print(mat(matrix))

# O(M + N)
def mat_pathfinder(matrix):
    # Start from top-left coner and going to the bottom left corner
    memo = -1
    step = 1
    lower_bounder = 0
    left_bounder = len(matrix[0]) - 1
    while lower_bounder <= len(matrix) - 1 and left_bounder >= 0:
        if matrix[lower_bounder][left_bounder] == 1:
            memo = left_bounder
            left_bounder -= step
        elif matrix[lower_bounder][left_bounder] == 0:
            lower_bounder += step
    return memo

mat_pathfinder(matrix)
