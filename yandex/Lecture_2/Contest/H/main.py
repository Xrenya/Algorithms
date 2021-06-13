import numpy as np
x = [2, 4, 0, 3, 1]

# Solution: i-th order statistic 
# Rewrite it in function 
max_1 = np.partition(np.asarray(x), k)[len(x)-1])
max_2 = np.partition(np.asarray(x), k)[len(x)-2])
max_2 = np.partition(np.asarray(x), k)[len(x)-3])

min_1 = np.partition(np.asarray(x), k)[0])
min_2 = np.partition(np.asarray(x), k)[1])


if max_1*max_2*max_3 > min_1*min_2*max_1:
    print(max_1, max_2, max_3)
else:
    print(min_1, min_2, max_1)
