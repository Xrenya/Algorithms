class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        running_sum = 0
        
        for i, num in enumerate(nums):
            running_sum <<= 1 
            running_sum += num #
            

            nums[i] = running_sum % 5 == 0
            
        return nums


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        last = "0"
        output = []
        for i in range(1, len(nums) + 1):
            last = last + str(nums[i - 1])
            output.append(int(last, 2) % 5 == 0)
        return output
