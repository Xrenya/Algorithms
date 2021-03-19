class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Memory efficient but slow
        # Time complexity O(n^2)
        acc = []
        for i in range(len(nums)):
            runningSum = 0
            while i > -1:
                runningSum += nums[i]
                i -= 1
            acc.append(runningSum)
        return acc
      
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Time complexity O(n)
        acc = []
        runningSum = 0
        for num in nums:
            runningSum += num
            acc.append(runningSum)
        return acc
