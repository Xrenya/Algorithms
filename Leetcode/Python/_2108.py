class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_palidrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        for s in words:
            if is_palidrome(s, 0, len(s) - 1):
                return s

        return ""
        
