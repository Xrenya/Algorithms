class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word):
            alphabet = [0] * 26
            for letter in word:
                alphabet[ord(letter) - ord('a')] += 1
            return alphabet
        
        bmax = [0] * 26
        for word in words2:
            for i, c in enumerate(count(word)):
                bmax[i] = max(bmax[i], c)

        output = []
        for char in words1:
            if all(x >= y for x, y in zip(count(char), bmax)):
                output.append(char)
        return output
