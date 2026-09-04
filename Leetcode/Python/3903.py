class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suffix = [float("inf")] * n
        suffix[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = min(suffix[i + 1], nums[i])
        dist = float("inf")
        cmax = nums[0]
        for i in range(n):
            cmax = max(cmax, nums[i])
            cdist = abs(cmax - suffix[i])
            if dist > cdist:
                dist = cdist
                if dist <= k:
                    return i
        return -1

        
