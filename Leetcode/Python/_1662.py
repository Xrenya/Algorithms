class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)
      
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string1 = ""
        string2 = ""
        for string in word1:
            string1 += string
        for string in word2:
            string2 += string
        return string1 == string2
