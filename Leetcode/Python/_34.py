class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binsearch(arr, target, lower=True):
            l = -1
            r = len(arr)
            while l < r - 1:
                m = l + (r - l) // 2
                if lower:
                    if arr[m] < target:
                        l = m
                    else:
                        r = m
                else:
                    if arr[m] <= target:
                        l = m
                    else:
                        r = m
            return r if lower else l

        left = binsearch(nums, target, True)
        right = binsearch(nums, target, False)
        if 0 <= left < len(nums) and left <= right and nums[left] == target:
            return [left, right]
        return [-1, -1]


class Solution:
    def searchRange(self, nums, target):
        def get_boundary(nums, target, lower):
            n = len(nums)
            if 1 > n:
                return -1
            l = -1
            r = n
            while l < r - 1:
                m = l + (r - l) // 2
                if lower:
                    if nums[m] >= target:
                        r = m
                    else:
                        l = m
                else:
                    if nums[m] > target:
                        r = m
                    else:
                        l = m
            return r if lower else l
        left = get_boundary(nums, target, True)
        if left == -1 or left == len(nums):
            return [-1, -1]
        elif nums[left] != target:
            return [-1, -1]
        right = get_boundary(nums, target, False)
        return [left, right]
