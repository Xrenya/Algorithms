class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cnt, max_len = 0, 0
        memo = {0: -1}
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt -= 1
            else:
                cnt += 1
            
            if cnt in memo:
                max_len = max(max_len, i - memo[cnt])
            else:
                memo[cnt] = i
                
        return max_len
