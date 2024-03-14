class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cur, count = 0, 0
        freq = {}

        for num in nums:
            cur += num
            if cur == goal:
                count += 1

            if cur - goal in freq:
                count += freq[cur - goal]

            freq[cur] = freq.get(cur, 0) + 1
        
        return count
