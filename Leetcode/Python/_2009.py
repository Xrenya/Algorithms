class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        output = n
        new_nums = sorted(set(nums))
        j = 0
        len_new_nums = len(new_nums)
        for i in range(len_new_nums):
            while j < len_new_nums and new_nums[j] < new_nums[i] + n:
                j += 1
            count = j - i
            output = min(output, n - count)
    
        return output
