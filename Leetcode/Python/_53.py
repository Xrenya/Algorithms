class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        cur_sum = 0

        for num in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += num
            maxSub = max(maxSub, cur_sum)
            print(maxSub)
        return maxSub
