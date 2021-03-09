class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time complexity O(n)
        hashMap = {} # value: index
        
        for i in range(len(nums)):
            if hashMap.get(target - nums[i]) is not None:
                return [hashMap.get(target - nums[i]), i]
            else: 
                hashMap[nums[i]] = i
                
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # Time complexity O(n^2)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i, j]
