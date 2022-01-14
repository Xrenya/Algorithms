# Слияние отрезков:
#
# Вход: [1, 3] [100, 200] [2, 4]
# Выход: [1, 4] [100, 200]
nums = [[1, 3], [100, 200], [2, 4], [1, 1], [0, 301]]
def merge(nums):
    last = None
    output = []
    for num in sorted(nums):
        if last is None:
            last = num
            output.append(num)
        else:
            if num[0] <= last[-1] and num[-1] >= last[-1]:
                output[-1][-1] = num[-1]
            elif num[0] >= last[0] and num[-1] <= last[-1]:
                continue
            else:
                output.append(num)
    return output


print(merge(nums))
