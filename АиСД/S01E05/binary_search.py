

def bin_less_or_equal_target(nums, target):
    l = -1
    r = len(nums)
    while r > l + 1:
        m = l + (r - l) // 2
        if nums[m] > target:
            r = m
        else:
            l = m

    return nums[l]

nums = [1,4,5,6,7,8]
target = 3
print(bin_less_or_equal_target(nums, target))  # 1


def bin_more_or_equal_target(nums, target):
    l = -1
    r = len(nums)
    while r > l + 1:
        m = l + (r - l) // 2
        if nums[m] >= target:
            r = m
        else:
            l = m

    return nums[l]

nums = [1,4,5,6,7,8]
target = 3
print(bin_more_or_equal_target(nums, target))  # 4
