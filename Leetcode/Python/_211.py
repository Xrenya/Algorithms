class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        trie = self.trie
        for char in word:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie["$"] = True
        
        

    def search(self, word: str) -> bool:
        def recursive_call(word, node):
            for i, char in enumerate(word):
                if not char in node:
                    if char == ".":
                        for x in node:
                            if x != "$" and recursive_call(word[i + 1:], node[x]):
                                return True

                    return False
                else:
                    node = node[char]

            return "$" in node
        return recursive_call(word, self.trie)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

class WordDictionary:

    def __init__(self):
        self.vocab = dict()

    def addWord(self, word: str) -> None:
        if len(word) not in self.vocab:
            self.vocab[len(word)] = set()
        self.vocab[len(word)].add(word)

    def search(self, word: str) -> bool:
        if len(word) not in self.vocab:
            return False
        
        if '.' in word:
            for w in self.vocab[len(word)]:
                temp = True
                for i in range(len(w)):
                    if word[i] != '.' and word[i] != w[i]:
                        temp = False
                        break
                if temp:
                    return temp
            return False
        else:
            if word in self.vocab[len(word)]:
                return True
            return False
