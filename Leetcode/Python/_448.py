class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            pos = nums[i] - 1
            if nums[i] != nums[pos]:
                nums[i], nums[pos] = nums[pos],  nums[i]
            else:
                i += 1
        
        output = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                output.append(i + 1)
        return output
            
