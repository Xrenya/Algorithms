class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26

        for i in range(len(s)):
            cur = ord(s[i]) - ord("a")
            if first[cur] == -1:
                first[cur] = i
            
            last[cur] = i

        output = 0

        for i in range(26):
            if first[i] == -1:
                continue

            between = set()

            for j in range(first[i] + 1, last[i]):
                between.add(s[j])

            output += len(between)

        return output
