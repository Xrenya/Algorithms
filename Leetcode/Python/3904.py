class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suffix = [0] * n
        suffix[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix[i] = min(suffix[i + 1], nums[i])

        output = -1
        min_value= float("inf")
        largest = -float("inf")
        for i in range(n):
            if largest < nums[i]:
                largest = nums[i]
            cmin = largest - suffix[i]
            if cmin <= k:
                if cmin < min_value:
                    return i
        return -1
