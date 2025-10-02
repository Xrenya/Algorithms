class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        epmty = numBottles
        counter = numBottles
        while epmty >= numExchange:
            counter += 1
            epmty -= numExchange - 1
            numExchange += 1
        return counter
