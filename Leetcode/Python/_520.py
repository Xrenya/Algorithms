class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capitals = 0
        for char in word:
            if char.isupper():
                capitals += 1
        if capitals == 1 and word[0].isupper():
            return True
        elif capitals == 0:
            return True
        elif capitals == len(word):
            return True
        else:
            return False
        
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        caps = False
        low = False
        first = False
        for i, c in enumerate(word):
            if i == 0:
                if c.isupper():
                    first = True
            else:
                if c.isupper():
                    caps = True
                else:
                    low = True
        if (low is True and caps is False and first is True) or (first is False and low is True and caps is False) or (first is True and low is False and caps is True) or len(word) == 1:
            return True
        return False
