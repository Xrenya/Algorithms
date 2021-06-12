a = int(input())
b = int(input())
n = int(input())
m = int(input())

def minmax(x, y):
    minval = (x+1) * (y-1) + 1
    maxval = (x+1) * (y-1) + 1 + 2 * x
    return minval, maxval
    
min1 = (a+1) * (n-1) + 1
max1 = (a+1) * (n-1) + 1 + 2 * a
min2 = (b+1) * (m-1) + 1
max2 = (b+1) * (m-1) + 1 + 2 * b

minans = max(min1, min2)
maxans = min(max1, max2)


if maxans < minans:
    print(-1)
else:
    print(minans, maxans)

