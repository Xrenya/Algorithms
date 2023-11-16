class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros: int = 0
        left: int = 0
        n: int = len(nums)
        max_ones: int = 0
        for right in range(n):
            if not nums[right]:
                zeros += 1

            while zeros > k:
                if not nums[left]:
                    zeros -= 1
                left += 1

            max_ones = max(max_ones, right - left + 1)

        return max_ones
            
