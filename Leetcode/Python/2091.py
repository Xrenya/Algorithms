class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_el = [nums[0], 0]
        max_el = [nums[0], 0]
        for i in range(1, len(nums)):
            if nums[i] > max_el[0]:
                max_el[0] = nums[i]
                max_el[1] = i
            if nums[i] < min_el[0]:
                min_el[0] = nums[i]
                min_el[1] = i

        min_del = len(nums)
        a = min(min_el[1], max_el[1])
        b = max(min_el[1], max_el[1])
        min_del = min(
            min_del,
            a + len(nums) - b + 1,
            b + 1,
            len(nums) - a
        )
        return min_del
