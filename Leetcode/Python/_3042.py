class Node:
    def __init__(self):
        self.links = [None] * 26

    def _contains(self, char: str) -> bool:
        return self.links[ord(char) - ord("a")] is not None

    def _put(self, char: str, node: "Node") -> None:
        self.links[ord(char) - ord("a")] = node

    def _next(self, char: str) -> "Node":
        return self.links[ord(char) - ord("a")]


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if not node._contains(char):
                node._put(char, Node())
            node = node._next(char)
    
    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if not node._contains(char):
                return False
            node = node._next(char)
        return True


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0

        for i in range(n):
            prefix_trie = Trie()
            suffix_trie = Trie()

            prefix_trie.insert(words[i])
            suffix_trie.insert(words[i][::-1])

            for j in range(i):
                if len(words[j]) > len(words[i]):
                    continue

                if (
                    prefix_trie.starts_with(words[j])
                    and suffix_trie.starts_with(words[j][::-1])
                ):
                    count += 1

        return count
