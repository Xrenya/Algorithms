class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(n):
            acc = 0
            while n:
                acc = acc * 10 + n % 10
                n //= 10

            return acc

        arr = []
        for i in range(len(nums)):
            arr.append(nums[i] - rev(nums[i]))

        MOD = 10**9 + 7
        mapping = defaultdict(int)
        output = 0
        for i in range(len(nums)):
            output = (output + mapping[arr[i]]) % MOD
            mapping[arr[i]] += 1
        return output
