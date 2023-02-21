class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = nums[0]
        for num in nums[1:]:
            n ^= num
            
        return n
