class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = 10**5 + 1
        max_p = 0
        cnt = 0
        for p in  prices:
            if p > max_p:
                max_p = p
            if p < min_p:
                min_p = p
                max_p = 0
            diff = max_p - min_p
            if cnt < diff:
                cnt = diff
        return cnt