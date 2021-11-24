nums = [1,2,3,4,5,6,7,8,9,10]


def binary_search(nums, target):
    l = -1
    r = len(nums)
    while l < r - 1:
        m = (l + r) >> 1 # to avoid overflow, it fast compared to l + (r - l) // 2 and stable compared to (l + r) // 2
        if nums[m] == target:
            return nums[m]
        elif nums[m] < target:
            l = m
        else:
            r = m
    if abs(target - nums[l]) < abs(nums[r] - target):
        return nums[l]
    else:
        return nums[r]

print(binary_search(nums=[0,1,10,11], target=6)) # 1,2,3,4,5 5,6,7,8,9,10
print(5 >> 1)
