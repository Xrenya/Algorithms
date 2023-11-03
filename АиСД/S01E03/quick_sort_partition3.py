import random

def quick_sort(a, l, r):
    if l >= r:
        return
    pivot_index = random.randint(l, r)
    a[pivot_index], a[l] = a[l], a[pivot_index]
    less_than, greater_than = partition3(a, l, r)
    quick_sort(a, l, less_than - 1)
    quick_sort(a, r, greater_than + 1)
    
def partition3(a, l, r):
    less_than = l
    i = l
    greater_than = r
    pivot = a[l]
    while i <= greater_than:
        if a[i] > pivot:
            a[greater_than], a[i] = a[i], a[greater_than]
            greater_than -=1
        elif a[i] < pivot:
            a[less_than], a[i] = a[i], a[less_than]
            less_than +=1
            i += 1
        else:
            i += 1
    return less_than, greater_than
            

    
a = [5, 1, 100, 2, 2, 2, 4, -1]
print(a)
quick_sort(a, 0, len(a) - 1)
print(a)
