class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote = 0
        result = None
        n = len(nums) // 2
        for num in nums:
            if vote == 0:
                result = num
            if result == num:
                vote += 1
                if vote > n:
                    return result
            else:
                vote -= 1
        return result
    
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote = 0
        result = None
        
        for num in nums:
            if vote == 0:
                result = num
            if result == num:
                vote += 1
            else:
                vote -= 1
        return result
    
    
from collections import defaultdict 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lenght = len(nums)
        major = lenght // 2
        hashMap = defaultdict(int)
        for num in nums:
            hashMap[num] += 1
            if hashMap[num] > major:
                return num
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        high = 0
        output = 0
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 0
            hashMap[num] += 1
            if high < hashMap[num]:
                high = hashMap[num]
                output = num
        return output
        
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = defaultdict(int)
        high = 0
        output = 0
        for num in nums:
            hashMap[num] += 1
            if high < hashMap[num]:
                high = hashMap[num]
                output = num
        return output
