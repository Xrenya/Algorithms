class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        prefix = [0] * (n + 1)

        for i in range(n):
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix[i + 1] = prefix[i] + 1
            else:
                prefix[i + 1] = prefix[i]
        output = [0] * len(queries)
        for idx, (sq, eq) in enumerate(queries):
            output[idx] = prefix[eq + 1] - prefix[sq]

        return output
