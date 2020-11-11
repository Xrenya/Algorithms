number = int(input())

def less(number):
    arr = []
    for i in range(1, number+1):
        if i**2 <= number:
            arr.append(str(i**2))
        else:
            break
    return " ".join(arr)

print(less(number))
