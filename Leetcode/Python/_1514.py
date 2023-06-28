class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        max_proba = [0] * n
        max_proba[start] = 1

        for i in range(n - 1):
            updated = 0
            for j in range(len(edges)):
                u, v = edges[j]
                path_prob = succProb[j]
                if max_proba[u] * path_prob > max_proba[v]:
                    max_proba[v] = max_proba[u] * path_prob
                    updated = 1
                if max_proba[v] * path_prob > max_proba[u]:
                    max_proba[u] = max_proba[v] * path_prob
                    updated = 1
            if not updated:
                break

        return max_proba[end]
