class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        zeros = [0] * n
        ones = [0] * n

        for i in range(n):
            if s[i] == "0":
                if i > 0:
                    zeros[i] = zeros[i - 1] + 1
                else:
                    zeros[i] = 1
            else:
                zeros[i] = zeros[i - 1]
            if s[n - i - 1] == "1":
                if i > 0:
                    ones[n - i - 1] = ones[n - i] + 1
                else:
                    ones[n - i - 1] = 1
            else:
                if i > 0:
                    ones[n - i - 1] = ones[n - i]

        max_score = 0
        for i in range(n - 1):
            max_score = max(max_score, zeros[i] + ones[i + 1])

        return max_score


class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        zeros = [0] * n
        ones = [0] * n
        for i in range(n):
            if s[i] == "0":
                if i > 0:
                    zeros[i] = zeros[i - 1] + 1
                else:
                    zeros[i] = 1
            else:
                zeros[i] = zeros[i - 1]
            if s[n - 1 - i] == "1":
                if n - 1 - i == n - 1:
                    ones[n - 1 - i] = 1
                else:
                    ones[n - 1 - i] = ones[n - i] + 1
            else:
                if n - 1 - i < n - 1:
                    ones[n - 1 - i] = ones[n - i]

        max_score = 0
        for i in range(n - 1):
            max_score = max(max_score, zeros[i] + ones[i + 1])
            
        return max_score
