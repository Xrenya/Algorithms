# Дан массив из нулей и единиц. Нужно определить, какой максимальный по длине подинтервал единиц можно получить, удалив ровно один элемент массива.
# [1, 1, 0]

def longestSubarray(nums) -> int:
    k = 1
    res = i = 0

    for j in range(0, len(nums)):
        print(nums[j], k)
        if nums[j] == 0:
            k -= 1
        if k < 0:
            if nums[i] == 0:
                k += 1
            i += 1
        res = max(res, (j - i))

    return res
  
 print(longestSubarray(nums))
