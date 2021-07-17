class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        cnt = nums[0]
        if cnt >= target:
            return 1
        ans = float("inf")
        dist = 0
        while l < len(nums):
            if cnt >= target:
                dist = r - l + 1
                if ans > dist:
                    ans = dist
            if cnt < target and r < len(nums)-1:
                r += 1
                cnt += nums[r]
            else:
                cnt -= nums[l]
                l += 1
        if ans == float("inf"):
            return 0
        return ans
