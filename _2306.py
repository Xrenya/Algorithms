class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        n = ord("z") - ord("a") + 1
        suffix = [set() for _ in range(n)]
        for word in ideas:
            letter = word[0]
            suffix[ord(letter) - ord("a")].add(word[1:])
        counter = 0
        for i in range(n):
            for j in range(i + 1, n):
                mutual = len(suffix[i] & suffix[j])
                counter += 2 * (len(suffix[i]) - mutual) * (len(suffix[j]) - mutual)

        return counter
