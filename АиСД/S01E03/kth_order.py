import random


def partition(nums, left, right):
    pivot = nums[random.randint(left, right)]
    while True:
        while nums[left] < pivot:
            left += 1

        while nums[right] > pivot:
            right -= 1

        if left >= right:
            return right

        nums[left], nums[right] = nums[right], nums[left]


def kth_order(nums, left, right, k):
    if left < right:
        random_index = partition(nums, left, right)
        if k <= random_index:
            return kth_order(nums, left, random_index, k)
        else:
            return kth_order(nums, random_index + 1, right, k)
    return nums[k]


nums = [1, 3, 2, -10, 4, 5, -1000]
kth = 1
print(kth_order(nums, 0, len(nums) - 1, kth - 1))
