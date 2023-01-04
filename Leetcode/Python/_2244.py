class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        mapping = defaultdict(int)
        for n in tasks:
            mapping[n] += 1
        rounds = 0
        for k, v in mapping.items():
            if v == 1:
                return -1
            if v % 3 == 0:
                rounds += v // 3
            else:
                rounds += v // 3 + 1
        return rounds
