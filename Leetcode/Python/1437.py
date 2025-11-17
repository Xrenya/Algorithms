class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        dist = float("inf")
        prev = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if dist < k:
                    return False
                prev = i
                dist = 0
            else:
                dist += 1
        return True
