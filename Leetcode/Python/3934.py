class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        MOD  = 1000000007
        BASE = 911382323

        n = len(nums)
        h = [0] * (n + 1)
        p = [0] * (n + 1)
        p[0] = 1

        for i in range(n):
            h[i + 1] = (h[i] * BASE + nums[i]) % MOD
            p[i + 1] = p[i] * BASE % MOD

        def check(length: int):
            count = {}
            for l in range(n - length + 1):
                r = l + length
                key = (h[r] - h[l] * p[length] % MOD + MOD) % MOD
                count[key] = count.get(key, 0) + 1

            for t in count.values():
                if t == 1:
                    return True
            return False


        left = 1
        right = n
        while left < right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
