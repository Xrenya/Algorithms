class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        output = []
        while len(nums) > 1:
            for i in range(len(nums) - 1):
                output.append((nums[i] + nums[i + 1]) % 10)
            nums = output
            output = []
        return nums.pop()
