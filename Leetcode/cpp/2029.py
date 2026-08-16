class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        zeros, ones, twos = 0, 0, 0
        for stone in stones:
            if stone % 3 == 0:
                zeros += 1
            elif stone % 3 == 1:
                ones += 1
            else:
                twos += 1
        if zeros % 2 == 0:
            return ones >= 1 and twos >= 1
        return ones - twos > 2 or twos - ones > 2
