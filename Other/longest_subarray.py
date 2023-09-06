# Дан массив из нулей и единиц. Нужно определить, какой максимальный по длине подинтервал единиц можно получить, удалив ровно один элемент массива.
# [1, 1, 0]

nums = [1, 0, 1, 1, 0, 0, 1, 1, 1, 1]

# Optimal solution
class Solution:
    def longestSubarray(self, nums) -> int:
        left = 0
        max_len = 0
        zeros = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros >= 2:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len - 1


def groupby(nums): # Group array into ones tuple of induces
    # [1, 0, 1, 1, 0, 0, 1, 1, 1, 1] --> [(-1, 0), (1, 3), (5, 9)]
    output = []
    first = -1
    last = 0
    for i, num in enumerate(nums + [0]):
        if num == 1:
            last = i
        else:
            if first != last:
                output.append((first, last))
            last, first = i, i
    return output


def dist(nums): # calculate distance if we remove one '0' and sum its len
    nums = groupby(nums)
    last = None
    max_len = 0
    for num in nums:
        if last is None:
            last = num
        else:
            if num[0] - last[-1] == 1:
                max_len = max(max_len, last[-1] - last[0] + num[-1] - num[0])
            else:
                max_len = max(max_len, num[-1] - num[0])
        last = num
    return max_len

print(dist(nums))

