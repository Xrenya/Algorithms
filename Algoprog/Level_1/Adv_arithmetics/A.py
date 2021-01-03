import numpy as np

def sits(array):
    return int(np.sum([np.ceil(np.array(array)/2)]))
array = [int(input()) for _ in range(3)]
sits(array)
