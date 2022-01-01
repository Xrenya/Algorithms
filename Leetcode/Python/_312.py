class Solution:
    
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        if len(nums) ==1:return nums[0]
        if len(set(nums)) ==1:
            return (nums[0]**3)*(len(nums)-2)+nums[0]**2+nums[0]
        nums =[1]+nums+[1]
        n=len(nums)
        dp=[[0]*n for i in range(n)]
        
        for left in range(n-2, 0,-1):
            for right in range(left,n-1):
                for i in range(left, right+1):
                    dp[left][right] = max(dp[left][i-1]+dp[i+1][right]+nums[left-1]*nums[i]*nums[right+1], dp[left][right])
        
        return dp[1][n-2]
