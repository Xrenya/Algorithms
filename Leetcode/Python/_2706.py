class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        count = [0] * 101
        for p in prices:
            count[p] += 1
            
        first_min, second_min = -1, -1
        for p in range(len(count)):
            if count[p] > 1:
                if 2 * p <= money:
                    return money - 2 * p
                return money
            elif count[p] == 1:
                count[p] -= 1
                first_min = p
                break
                
                
        for p in range(first_min, len(count)):
            if count[p] >= 1:
                if first_min + p <= money:
                    return money - (first_min + p)
                return money


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        
        min_cost = prices[0] + prices[1]
        
        if min_cost <= money:
            return money - min_cost
        return money
