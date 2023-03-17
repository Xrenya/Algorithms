class TrieNode:
    def __init__(self):
        self.letters = {}
        self.is_complete = False

    def get_keys(self):
        return list(self.letters.keys())

    def is_end(self):
        return self.is_complete

    def end(self):
        self.is_complete = True


class Trie:

    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        trie = self.trie
        for char in word:
            vocab = trie.get_keys()
            if char not in vocab:
                trie.letters[char] = TrieNode()
            trie = trie.letters[char]
        trie.end()
        return None


    def search(self, word: str) -> bool:
        trie = self.trie
        for char in word:
            vocab = trie.get_keys()
            if char not in vocab:
                return False
            trie = trie.letters[char]
        return trie.is_end()

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for char in prefix:
            vocab = trie.get_keys()
            if char not in vocab:
                return False
            trie = trie.letters[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
