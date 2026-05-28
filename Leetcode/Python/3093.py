class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_idx = -1
        self.best_len = float("inf")
        self.best_word_idx = float("inf")

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()

        def update(node, length, idx):
            if (length, idx) < (node.best_len, node.best_word_idx):
                node.best_len = length
                node.best_word_idx = idx
                node.best_idx = idx
                
        for i, word in enumerate(wordsContainer):
            update(root, len(word), i)

        for i, word in enumerate(wordsContainer):
            node = root
            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                update(node, len(word), i)

        output = []
        for word in wordsQuery:
            node = root
            for ch in reversed(word):
                if ch in node.children:
                    node = node.children[ch]
                else:
                    break
            output.append(node.best_idx)

        return output
