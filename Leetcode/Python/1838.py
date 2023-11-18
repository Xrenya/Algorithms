class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        cur, output = 0, 0

        for right in range(len(nums)):
            target = nums[right]
            cur += target

            while target * (right - left + 1) > cur + k:
                cur -= nums[left]
                left += 1

            output = max(output, right - left + 1)

        return output
