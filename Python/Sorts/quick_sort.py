import random


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
