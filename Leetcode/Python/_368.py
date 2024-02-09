class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []

        nums.sort()

        dp = [0] * len(nums)

        for i, num in enumerate(nums):
            max_size = 0
            for k in range(0, i):
                if nums[i] % nums[k] == 0:
                    max_size = max(max_size, dp[k])

            max_size += 1
            dp[i] = max_size

        max_size, max_size_idx = max([(v, i) for i, v in enumerate(dp)])

        output = []
        size, tail = max_size, nums[max_size_idx]
        for i in range(max_size_idx, -1, -1):
            if size == dp[i] and tail % nums[i] == 0:
                output.append(nums[i])
                size -= 1
                tail = nums[i]

        return reversed(output)
