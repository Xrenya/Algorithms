nums = [0, 4, 3, 2, 1]

for i in range(len(nums)):
    j = i
    while j > 0 and nums[j] < nums[j - 1]:
        nums[j], nums[j - 1] = nums[j - 1], nums[j]
        j -= 1

print(nums)
