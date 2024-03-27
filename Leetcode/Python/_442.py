class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        # Cycle sort O(n)
        while i < n:
            correct_idx = nums[i] - 1
            if nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1
                
        output = []
        for i in range(n):
            if nums[i] - 1 != i:
                output.append(nums[i])
                
        return output


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        
        for num in nums:
            if nums[abs(num) - 1] < 0:
                result.append(abs(num))
            nums[abs(num) - 1] *= -1    
            
        return result
