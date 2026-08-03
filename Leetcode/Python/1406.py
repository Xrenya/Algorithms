class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @lru_cache
        def dfs(index):
            if index >= len(stoneValue):
                return 0
            max_score = -float("inf")
            score = 0
            for i in range(3):
                if i + index >= len(stoneValue):
                    break
                score += stoneValue[index + i]
                max_score = max(max_score, score - dfs(index + i + 1))
            return max_score

        r = dfs(0)
        if r > 0:
            return "Alice"
        elif r < 0:
            return "Bob"
        return "Tie"
