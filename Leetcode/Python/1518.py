class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        counter = numBottles
        empty = 0
        while numBottles // numExchange > 0:
            add_bottle = numBottles // numExchange
            empty = numBottles % numExchange
            counter += add_bottle
            numBottles = add_bottle + empty
        return counter
