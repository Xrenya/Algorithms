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
