class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        prev_sum = 0
        output = -1
        for n in nums:
            if n < prev_sum:
                output = n + prev_sum
            prev_sum += n
        return output
