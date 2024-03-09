class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        mf = 0
        out = -1
        c = defaultdict(int)
        for n in nums:
            c[n] += 1
            if mf < c[n]:
                out = n
                mf = c[n]
        total = 0
        for k, v in c.items():
            if v == mf:
                total += 1
        return total * mf
