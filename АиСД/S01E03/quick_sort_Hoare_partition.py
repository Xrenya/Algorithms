import random


def qsort(array, left, right):
    if left < right:
        pivot = random.randint(left, right)
        random_index = partition(array, left, right)
        qsort(array, left, random_index)
        qsort(array, random_index + 1, right)


def partition(array, left, right):
    pivot = array[random.randint(left, right)]
    i = left
    j = right
    while True:
        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1
        if i >= j:
            return j

        array[i], array[j] = array[j], array[i]


array = [random.randint(-10, 100) for _ in range(5)]
left = 0
right = len(array) - 1
print(array)
qsort(array, left, right)
print(array)
