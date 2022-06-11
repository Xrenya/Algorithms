class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        left = 0
        current = 0
        maxlen = -1
        
        for right in range(len(nums)):
            current += nums[right]
            
            while current > total - x and left <= right:
                current -= nums[left]
                left += 1
                
            if current == total - x:
                maxlen = max(maxlen, right - left + 1)
                
        return len(nums) - maxlen if maxlen != -1 else -1
