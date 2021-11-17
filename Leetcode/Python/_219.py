class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}
        for i, num in enumerate(nums):
            if num not in hashMap:
                hashMap[num] = i
            else:
                if (i - hashMap[num]) <= k:
                    return True
                else:
                    hashMap[num] = i
        return False
