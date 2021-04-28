class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        lenght = len(searchWord)
        for i, word in enumerate(sentence.split(" ")):
            if searchWord == word[:lenght]:
                return i+1
        return -1
      
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split(" ")):
            if word.startswith(searchWord):
                return i+1
        return -1

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        lenght = len(searchWord)
        words = sentence.split(" ")
        for i, word in enumerate(words):
            if searchWord == word[:lenght]:
                return i+1
        return -1
