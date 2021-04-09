class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        prices += [0]
        array = []
        for i in range(len(prices)-1):
            j = i + 1
            while j < len(prices) and prices[j] > prices[i]:
                j += 1
            array.append(prices[i] - prices[j])
        return array
