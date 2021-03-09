class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # value: index
        
        for i in range(len(nums)):
            if hashMap.get(target - nums[i]) is not None:
                return [hashMap.get(target - nums[i]), i]
            else: 
                hashMap[nums[i]] = i
