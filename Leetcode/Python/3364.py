class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        best = float('inf')
        for length in range(l, r + 1):
            for i in range(n - length + 1):
                s = prefix[i + length] - prefix[i]
                if 0 < s < best:
                    best = s

        return -1 if best == float('inf') else best
