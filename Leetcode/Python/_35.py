class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = -1
        r = len(nums)
        while l < r - 1:
            m = l + (r - l) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m
        return r
    

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = -1
        r = len(nums)
        while l < r - 1:
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] > target:
                    r = mid 
                else:
                    l = mid 
        return r

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        if  nums[l] < target:
            return l + 1
        return l
        
