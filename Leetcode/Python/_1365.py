class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Time complexity O(n)
        # Since unique numbers are limited [0-100] in the array 
        # we create a lenght of the array 102.
        count = [0] * 102
        for num in nums:
            count[num+1] += 1
        for i in range(1, 102):
            count[i] += count[i-1]
        return [count[num] for num in nums]
