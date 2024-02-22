class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_to = [0] * n
        trust_from = [0] * n
        for from_, to_ in trust:
            trust_to[to_ - 1] += 1
            trust_from[from_ - 1] += 1
            
        for i in range(n):
            if trust_to[i] == n - 1 and trust_from[i] == 0:
                return i + 1
        return -1
