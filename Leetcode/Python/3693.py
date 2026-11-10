class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        best = [float("inf")] * (n + 1)
        best[0] = 0
        for j in range(1, n + 1):
            for k in (1, 2, 3):
                if j - k >= 0:
                    best[j] = min(best[j], best[j - k] + costs[j - 1] + k * k)
        return best[n]
