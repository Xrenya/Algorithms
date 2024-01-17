# Given array with values [1..N]
# Some numbers are repeated twice and some are missing
# find the missing numbers
# [5, 2, 3, 7, 2, 1, 1] -> [4, 6]

array = [5, 2, 3, 7, 2, 1, 1]

def missing(array):
    n = len(array)
    index = 0
    while index < n:
        swap_index = array[index] - 1
        if array[index] == array[swap_index] or array[index] - 1 == index:
            index += 1
        else:
            array[index], array[swap_index] = array[swap_index], array[index]
    output = []
    for i in range(n):
        if array[i] - 1 != i:
            output.append(i + 1)
    return output

print(missing(array))
print("Correct output: ", [4, 6])
