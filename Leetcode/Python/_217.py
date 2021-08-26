class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 0
            hashMap[num] += 1
            if hashMap[num] >= 2:
                return True
        return False
