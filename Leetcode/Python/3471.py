class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == k:
            return max(nums)
        
        count = [0] * 51
        for num in nums:
            count[num] += 1
        
        if k == 1:
            for i in range(50, -1, -1):
                if count[i] == 1:
                    return i

        ret = -1
        if count[nums[0]] == 1:
            ret = max(ret, nums[0])
        if count[nums[-1]] == 1:
            ret = max(ret, nums[-1])
        return ret
