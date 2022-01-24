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
