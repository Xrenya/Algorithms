def sort2(first, second):
    if first < second:
        return (first, second)
    return (second, first)

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

a, b = sort2(a, b)
b, c = sort2(b, c)
a, b = sort2(a, b)
d, e = sort2(d, e)
if a <= d and b <= e:
    print('YES')
else:
    print('NO')
    
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
                array[j], array[j+1] =array[j+1], array[j]
                swapped = True
            
        if swapped is False:
            break
    return array
  
a, b, c = bubble_sort([a, b, c)
if a <= d and b <= e:
    print('YES')
else:
    print('NO')
