class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = -1 
        r = len(nums)
        while l < r - 1:
            m = (r + l) >> 1
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m
            else:
                r = m
        return -1
    
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
    
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = -1
        r = len(nums)
        while l < r - 1:
            m = (l + r) >> 1
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m
            else:
                r = m
        return -1
