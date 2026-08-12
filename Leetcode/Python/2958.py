class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        mapping = defaultdict(int)
        left = 0
        max_len = 0
        for right in range(len(nums)):
            num = nums[right]
            mapping[num] += 1
            while mapping[num] > k:
                remove_num = nums[left]
                mapping[remove_num] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
