num = int(input())

def even(n):
    arr = []
    for number in range(1, n+1):
        if n%number == 0:
            arr.append(str(number))
    return " ".join(arr)
    

print(even(num))
