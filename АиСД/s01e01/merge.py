a = [1,3,5]
b = [2,4,6]

def merge(a, b):
    i = 0
    j = 0
    while i < len(a) or j < len(b):
        if j == len(b) or (i < len(a) and a[i] < b[j]):
            c[i + j] =  a[i]
            i += 1
        else:
            c[i + j] = b[j]
            j += 1
    return c
c = [0, 0, 0, 0, 0, 0]
print(merge(a, b))
