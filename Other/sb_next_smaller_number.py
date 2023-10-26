# https://www.codewars.com/kata/5659c6d896bc135c4c00021e/train/python
# next_smaller(21) == 12
# next_smaller(531) == 513
# next_smaller(2071) == 2017
# next_smaller(9) == -1
# next_smaller(135) == -1
# next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros


def next_smaller(n):
    arr = [int(x) for x in str(n)]
    # if it is single digit then there is no way to swap
    # also if it is ascending array then it is not possible to get
    # the smallest value since it is already smallest possible digit
    if len(arr) == 1 or arr == sorted(arr):
        return -1
    size = len(arr)
    index = -1
    for i in range(size - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            index = i - 1
            break

    swap_index = index
    smallest = float("-inf")
    for i in range(index + 1, size):
        if arr[i] < arr[index] and arr[i] > smallest:
            smallest = arr[i]
            swap_index = i
    # swam digits with closes smallest digit which is less than value in index position
    # and at the same time it is the highest value amongst values after the index position 
    arr[index], arr[swap_index] = arr[swap_index], arr[index]
    sorted_arr = sorted(arr[index + 1:], reverse=True)
    for i in range(len(sorted_arr)):
        # after swapping sort the digit in descending to make it close the original digit
        arr[i + index + 1] = sorted_arr[i]

    digit = "".join(map(str, arr))
    # no leading zeros in digit
    return int(digit) if digit[0] != "0" else -1
