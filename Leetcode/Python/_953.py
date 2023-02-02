class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def compare(w1, w2):
            for char1, char2 in zip(w1, w2):
                if mapping[char1] > mapping[char2]:
                    return False
                elif mapping[char1] < mapping[char2]:
                    return True
            return True if len(w1) <= len(w2) else False

        mapping = {k: v for v, k in enumerate(order)}
        n = len(words)
        for i in range(n - 1):
            if not compare(words[i], words[i + 1]):
                return False
            
        return True
