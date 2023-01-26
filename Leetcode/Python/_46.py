class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first):
            if first == n:
                output.append(nums[:])
                return
            for i in range(first, n):
                nums[i], nums[first] = nums[first], nums[i] 
                backtrack(first + 1)
                nums[i], nums[first] = nums[first], nums[i] 
            return

        output = []
        n = len(nums)
        backtrack(0)
        return output
    
    
class Solution:
    result = []
    
    def backtrack(self, current, nums):
        if current == len(nums):
            self.result.append(nums[:])
            return

        for i in range(current, len(nums)):
            nums[i], nums[current] = nums[current], nums[i]
            self.backtrack(current + 1, nums)
            nums[i], nums[current] = nums[current], nums[i]
  
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.backtrack(0, nums)
        return self.result
