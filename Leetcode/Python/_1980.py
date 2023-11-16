class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def generate(cur):
            if len(cur) == n:
                if cur not in nums:
                    return cur
                return ""

            add_zeros = generate(cur + "0")
            if add_zeros:
                return add_zeros

            return generate(cur + "1")

        n = len(nums)
        nums = set(nums)
        return generate("")
