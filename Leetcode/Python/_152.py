class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max, cur_min = 1, 1
        maximum = nums[0]
        
        for n in nums:
            outputs = (n, n * cur_max, n * cur_min)
            cur_max, cur_min = max(outputs), min(outputs)
			
            maximum = max(maximum, cur_max)
            
        return maximum
