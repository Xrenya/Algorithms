def bubble_sort(array):
    n = len(array)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False
        
        # Last i elements are already in place 
        for j in range(0, n-i-1):
            # Traverse from 0 to n-i-1
            # Swap if the element found is 
            # greated than the next element
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
            
        if swapped is False:
            break
    return array

arr = [64, 34, 25]
  
print(bubble_sort(arr))
