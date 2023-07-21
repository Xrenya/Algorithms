class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lenght = [1] * n
        count = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lenght[j] + 1 > lenght[i]:
                        lenght[i] = lenght[j] + 1
                        count[i] = 0
                    if lenght[j] + 1 == lenght[i]:
                        count[i] += count[j]
                        
        max_len = max(lenght)
        ans = 0
        
        for i in range(n):
            if lenght[i] == max_len:
                ans += count[i]
        return ans
