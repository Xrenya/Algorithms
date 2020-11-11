num_1 = int(input())
num_2 = int(input())

def maximum(num_1, num_2):
    if num_1 > num_2:
        return num_1
    else:
        return num_2
    
print(maximum(num_1, num_2))
