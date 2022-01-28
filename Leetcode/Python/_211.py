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
