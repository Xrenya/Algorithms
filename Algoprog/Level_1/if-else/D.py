num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

def maximum(num_1, num_2, num_3):
    if num_1 > num_2:
        if num_1 > num_3:
            return num_1
        else:
            num_3
    else:
        if num_2 > num_3:
            return num_2
        else:
            return num_3
    
print(maximum(num_1, num_2, num_3))
