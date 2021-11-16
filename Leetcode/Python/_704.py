class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid
        if nums[l] == target:
            return l
        return -1
