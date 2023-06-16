class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7

        def dfs(nums):
            m = len(nums)
            if m < 3:
                return 1
            left_nodes = [n for n in nums if n < nums[0]]
            right_nodes = [n for n in nums if n > nums[0]]
            return dfs(left_nodes) * dfs(right_nodes) * comb(m - 1, len(left_nodes)) % mod

        return (dfs(nums) - 1) % mod
