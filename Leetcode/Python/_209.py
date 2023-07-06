class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        min_len = float("inf")
        cur_len = 0
        acc = 0
        for right in range(n):
            acc += nums[right]
            cur_len += 1
            while acc >= target:
                min_len = min(min_len, cur_len)
                acc -= nums[left]
                cur_len -= 1
                left += 1

        return 0 if min_len == float("inf") else min_len


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
