class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res 

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap = {}
        array = []
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        sorted_keys = sorted(hashMap, key=hashMap.get) 
        return sorted_keys[0]
                
