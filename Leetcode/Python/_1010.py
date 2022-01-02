class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dp = [0] * 60
        output = 0
        for t in time:
            reminder = t % 60
            target = (60 - reminder) % 60
            output += dp[target]
            dp[output] += 1
        return output
