class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_el = max(nums)
        ans = start = max_el_window = 0

        for end in range(len(nums)):
            if nums[end] == max_el:
                max_el_window += 1
            while max_el_window == k:
                if nums[start] == max_el:
                    max_el_window -= 1
                start += 1
            ans += start
        return ans
