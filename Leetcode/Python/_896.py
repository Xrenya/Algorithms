class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase = decrease = True
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                increase = False
            elif nums[i - 1] > nums[i]:
                decrease = False
        return increase or decrease
        
