class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev = None
        curr = 0
        longest = 0
        for n in nums:
            if n:
                curr += 1
            else:
                if prev is None:
                    prev = 0
                longest = max(longest, prev + curr)
                prev = curr
                curr = 0
        if prev is None:
            return curr - 1
        return max(longest, prev + curr)


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        array = []
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] == 1:
                while right < n and nums[right]:
                    right += 1
                array.append((left, right))
                left = right
            else:
                right += 1
                left = right

        if len(array) == 0:
            return 0
        elif len(array) == 1:
            ones = array[0]
            if len(nums) == ones[1] - ones[0]:
                return ones[1] - ones[0] - 1
            else:
                return ones[1] - ones[0]

        max_len = 0
        for i in range(len(array) - 1):
            firsts_1 = array[i]
            seconds_1 = array[i + 1]
            if seconds_1[0] - firsts_1[1] == 1:
                max_len = max(max_len, firsts_1[1] - firsts_1[0] + seconds_1[1] - seconds_1[0])
            else:
                max_len = max(max_len, firsts_1[1] - firsts_1[0], seconds_1[1] - seconds_1[0])
        return max_len


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        max_len, i = 0, 0

        for j in range(len(nums)):
            if nums[j] == 0:
                k -= 1
            if k < 0:
                if nums[i] == 0:
                    k += 1
                i += 1
            max_len = max(max_len, j - i)

        return max_len
