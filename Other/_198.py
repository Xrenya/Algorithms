class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        for i in range(1, len(dp)):
            dp[i] = max(nums[i - 1] + dp[i - 2] if i > 1 else nums[i - 1], dp[i - 1])
        
        return max(dp)
      
    def rob_rec(self, nums: List[int]) -> int:
        def recusive(position):
            if position >= len(nums):
                return 0

            if position in self.memo:
                return self.memo[position]
            
            output = max(recusive(position + 1), recusive(position + 2) + nums[position])

            self.memo[position] = output
            return output

        self.memo = {}
        return recusive(0)
