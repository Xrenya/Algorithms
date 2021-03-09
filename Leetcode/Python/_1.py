class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time complexity O(n)
        hashMap = {} # value: index
        
        for i in range(len(nums)):
            if hashMap.get(target - nums[i]) is not None:
                # if the differene is in the dictionary it will return the position
                return [hashMap.get(target - nums[i]), i]
            else: 
                # if the difference is not in the dictionary it will be added
                hashMap[nums[i]] = i 
                
    def bruteForceTwoSum(self, nums: List[int], target: int) -> List[int]:
    # Time complexity O(n^2)
        for i in range(len(nums)-1): # not including the last element
            for j in range(i+1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i, j]
