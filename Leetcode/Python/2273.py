class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        output = [words[0]]

        n = len(words)

        def compare(word1, word2):
            f = [0] * 26
            for w in word1:
                f[ord(w) - ord("a")] += 1
            for w in word2:
                f[ord(w) - ord("a")] -= 1
            return all(x == 0 for x in f)

        for i in range(1, n):
            if compare(words[i], words[i - 1]):
                continue
            output.append(words[i])
        return output
