class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i: int = 0
        n: int = len(prices)
        valley: int = prices[0]
        peak: int = prices[0]
        max_profit: int = 0
        while i < n - 1:
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            while i < n - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            max_profit += peak - valley
        return max_profit
