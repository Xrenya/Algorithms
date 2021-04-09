class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hashMap = {}
        acc = 0
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        for key in hashMap.keys():
            if hashMap[key] == 1:
                acc += key
        return acc
