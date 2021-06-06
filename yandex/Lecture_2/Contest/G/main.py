array = [int(x) for x in input().split()]
def mult(array):
    if len(array) == 2:
        return min(array), max(array)
    max_min_1 = 0
    max_min_2 = 0

    max_pos_1 = -1
    max_pos_2 = -1

    for num in array:
        if num < 0:
            if max_min_1 == 0:
                max_min_1 = num
            else:
                if max_min_1 >= num:
                    max_min_2 = max_min_1
                    max_min_1 = num
                elif max_min_2 >= num:
                    max_min_2 = num
        if num > 0:
            if max_pos_1 == -1:
                max_pos_1 = num
            else:
                if max_pos_1 <= num:
                    max_pos_2 = max_pos_1
                    max_pos_1 = num
                elif max_pos_2 <= num:
                    max_pos_2 = num
    if max_min_1 * max_min_2 > max_pos_1 * max_pos_2:
        return min(max_min_1, max_min_2), max(max_min_1, max_min_2)
    else:
        return min(max_pos_1, max_pos_2), max(max_pos_1, max_pos_2)
N1, N2 = mult(array)          
print(N1, N2)
