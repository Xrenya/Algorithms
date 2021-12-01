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
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p_min = prices[0]
        p_return = 0

        for price in prices:
            if price < p_min:
                p_min = price
            else:
                p_return = max(p_return, price - p_min)
        return p_return
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        first = float("inf")
        for num in prices:
            if first > num:
                first = num
            else:
                diff = num - first
                if diff > max_profit:
                    max_profit = diff
        return max_profit
