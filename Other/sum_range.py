# Дан список интов и число-цель. Нужно найти такой range, чтобы сумма его элементов давала число-цель.
#
# elements = [1, -3, 4, 5]
#
# target = 9
#
# result = range(2, 4) # because elements[2] + elements[3] == target

def sum_range(arr, target):
    prefix = [0] + arr
    mapping = {}
    for i in range(1, len(prefix)):
        prefix[i] += prefix[i - 1]
        if (target - prefix[i]) in mapping:
            return [mapping[target - prefix[i]], i]
        mapping[prefix[i]] = i - 1
    return [-1, -1]
