class Solution:
    def smallestPalindrome(self, s: str) -> str:
        l = len(s) // 2
        base = sorted(s[:l])
        mid = [s[l]] if len(s) % 2 else []
        tail = base[::-1]
        return "".join(base + mid + tail)
