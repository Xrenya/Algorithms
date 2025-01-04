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


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        ans = 0
        
        for letter in letters:
            i, j = s.index(letter), s.rindex(letter)
            between = set()
            
            for k in range(i + 1, j):
                between.add(s[k])
            
            ans += len(between)

        return ans
        
