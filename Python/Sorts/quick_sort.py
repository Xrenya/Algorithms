import random


def partition(arr, left, right):
    random_pivot = random.randint(left, right)
    arr[left], arr[random_pivot] = arr[random_pivot], arr[left]

    pivot_index = left

    i = left + 1
    for j in range(pivot_index + 1, right + 1):
        if arr[j] <= arr[pivot_index]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[pivot_index], arr[i - 1] = arr[i - 1], arr[pivot_index]
    pivot_index = i - 1
    return pivot_index


def quicksort_inplace(arr, left, right):
    """Randomized quicksort in-place instead of copying data into new array
    >>> array = [5,4,3,2,1]
    >>> quicksort(array, 0, len(array) - 1)
    [1, 2, 3, 4, 5]
    """
    if left < right :
        pivot_index = partition(arr, left, right)
        quicksort_inplace(arr, left, pivot_index - 1)
        quicksort_inplace(arr, pivot_index + 1, right)
        
        
def randomized_quicksort(arr):
    """
    This function takes an array as input and returns a sorted array using quicksort algorithm
    """
    # base case: if the array has less than two elements, it is already sorted
    if len(arr) < 2:
        return arr

    # choose the random pivot element's index
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    # partition the array into two subarrays based on the pivot element
    left = [arr[idx] for idx in range(len(arr)) if arr[idx] <= pivot and idx != pivot_index]
    right = [arr[idx] for idx in range(len(arr)) if arr[idx] > pivot and idx != pivot_index]

    # recursive calls to quicksort on left and right subarrays
    left_sorted = randomized_quicksort(left)
    right_sorted = randomized_quicksort(right)

    # concatenate the sorted subarrays with the pivot element in between
    return left_sorted + [pivot] + right_sorted


def quicksort(arr):
    """
    This function takes an array as input and returns a sorted array using quicksort algorithm
    """
    # base case: if the array has less than two elements, it is already sorted
    if len(arr) < 2:
        return arr
    
    # choose the pivot element
    pivot = arr[0]
    
    # partition the array into two subarrays based on the pivot element
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    
    # recursive calls to quicksort on left and right subarrays
    left_sorted = quicksort(left)
    right_sorted = quicksort(right)
    
    # concatenate the sorted subarrays with the pivot element in between
    return left_sorted + [pivot] + right_sorted
