class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = deque([0])
        seen = set()
        words = set(wordDict)

        while q:
            start = q.popleft()
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if end in seen:
                    continue

                if s[start:end] in words:
                    q.append(end)
                    seen.add(end)
        return False
