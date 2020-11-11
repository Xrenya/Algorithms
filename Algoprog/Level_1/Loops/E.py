arr = [int(x) for x in input().split()]

def zero(n):
    arr = []
    for number in n:
        if number == 0:
            return "YES"
    return "NO"
    
print(zero(arr))
