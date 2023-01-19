class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = 0
        output = 0
        prefix_mod = [0] * k
        prefix_mod[0] = 1

        for i in range(n):
            prefix = (prefix + nums[i] % k + k) % k
            output += prefix_mod[prefix]
            prefix_mod[prefix] += 1

        return output
