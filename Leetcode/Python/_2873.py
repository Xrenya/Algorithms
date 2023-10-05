class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        suffix = [0] * n
        suffix[-1] = nums[-1]
        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], nums[i])
            suffix[n - 1 - i] = max(suffix[n - i], nums[n - 1 - i])
        output = float("-inf")
        for i in range(1, n - 1):
            output = max(output, (prefix[i - 1] - nums[i]) * suffix[i + 1])
        return output if output >= 0 else 0 
