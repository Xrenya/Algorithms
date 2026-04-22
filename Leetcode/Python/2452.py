class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.is_end = False


class Solution:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word):
        trie = self.trie
        for char in word:
            idx = ord(char) - ord('a')
            if trie.child[idx] is None:
                trie.child[idx] = TrieNode()
            trie = trie.child[idx]
        trie.is_end = True

    def dfs(self, word, i, node, changes):
        if changes > 2 or not node:
            return False
        
        if i == len(word):
            return node.is_end

        index = ord(word[i]) - ord('a')

        if node.child[index] and self.dfs(word, i + 1, node.child[index], changes):
            return True

        if changes < 2:
            for c in range(26):
                if c == index:
                    continue
                if node.child[c] and self.dfs(word, i + 1, node.child[c], changes + 1):
                    return True
        return False

    def twoEditWords(self, queries, dictionary):
        for w in dictionary:
            self.insert(w)

        output = []
        for q in queries:
            if self.dfs(q, 0, self.trie, 0):
                output.append(q)
        return output
