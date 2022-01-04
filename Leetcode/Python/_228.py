class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def repr(a, b):
            if a == b:
                return f"{a}"
            else:
                return f"{a}->{b}"
        if len(nums) == 0:
            return []
        first = nums[0]
        last = nums[0]
        output = []
        for num in nums[1:]:
            if num - last == 1:
                last = num
            else:
                output.append(repr(first, last))
                first = num
                last = num
        output.append(repr(first, last))
        return output
