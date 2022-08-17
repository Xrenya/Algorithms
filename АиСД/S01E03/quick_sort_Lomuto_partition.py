import random


def select_random(left, right):
    return random.randint(left, right)

def select_last(left, right):
    return right

def select_first(left, right):
    return left

def qsort(array, left, right):
    if left < right:
        pivot = select_random(left, right)
        array[pivot], array[right] = array[right], array[pivot]
        m = partition(array, left, right)
        qsort(array, left, m - 1)
        qsort(array, m + 1, right)

def partition(array, left, right):
    i = left
    pivot_value = array[right]
    for j in range(left, right):
        if array[j] < pivot_value:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[right], array[i] = array[i], array[right]
    return i

array = [random.randint(-10, 100) for _ in range(5)]
left = 0
right = len(array) - 1
print(array)
qsort(array, left, right)
print(array)
