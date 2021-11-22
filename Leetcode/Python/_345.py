class Solution:
    def reverseVowels(self, s: str) -> str:
        LETTERS = ["e", "a", "i", "u", "o", "E", "A", "I", "U", "O"]
        l = 0
        r = len(s) - 1
        s = self.convert(s)
        print(s)
        while l < r:
            if s[l] not in LETTERS:
                l += 1
            if s[r] not in LETTERS:
                r -= 1
            if s[l] in LETTERS and s[r] in LETTERS:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return "".join(s)
                
    def convert(self, string):
        list1 = []
        list1[:0] = string
        return list1
                
