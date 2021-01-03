import math

def sits(array):
    return sum([math.ceil(num/2) for num in array])
array = [int(input()) for _ in range(3)]
sits(array)
