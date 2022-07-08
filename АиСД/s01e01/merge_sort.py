

a = [1,3,5,0,10,-1]

def merge(a, b):
    i = 0
    j = 0
    c = [0] * (len(a) + len(b))
    while i < len(a) or j < len(b):
        if j == len(b) or (i < len(a) and a[i] < b[j]):
            c[i + j] =  a[i]
            i += 1
        else:
            c[i + j] = b[j]
            j += 1
    return c
    
def sort(a):
    n = len(a)
    if n <= 1:
        return a
    pivot = len(a) // 2
    l = sort(a[:pivot])
    r = sort(a[pivot:])
    return merge(l, r)

print(sort(a))
