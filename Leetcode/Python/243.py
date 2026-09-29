class Solution:
    def shortestDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        mapping = defaultdict(list)
        for i, word in enumerate(wordsDict):
            mapping[word].append(i)
        min_distance = float('inf')
        for i in mapping[word1]:
            for j in mapping[word2]:
                min_distance = min(min_distance, abs(i - j))
        return min_distance
