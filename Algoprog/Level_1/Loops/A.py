num_1 = int(input())
num_2 = int(input())

def even(num_1, num_2):
    arr = []
    for i in range(num_1, num_2+1):
        if i%2 == 0:
            arr.append(str(i))
    return " ".join(arr)

print(even(num_1, num_2))
