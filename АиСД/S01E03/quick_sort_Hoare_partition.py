import random


def qsort(array, low, high):
    if left < right:
        pivot = random.randint(low, high)
        random_index = partition(array, low, high)
        qsort(array, low, random_index)
        qsort(array, random_index + 1, high)


def partition(a, low, high):
    pivot = a[random.randint(low, high)]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while a[i] < pivot:
            i += 1
            
        j -= 1
        while a[j] > pivot:
            j -= 1
            
        if i >= j:
            return j
        a[i], a[j] = a[j], a[i]



array = [random.randint(-10, 100) for _ in range(5)]
low = 0
high = len(array) - 1
print(array)
qsort(array, low, high)
print(array)
