class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....",
                 "..",".---","-.-",".-..","--","-.","---",".--.",
                 "--.-",".-.","...","-","..-","...-",".--","-..-",
                 "-.--","--.."]
        start_idx = 97
        newlst = []
        for i in words:
            newword = ""
            for j in i:
                idx = ord(j) - start_idx
                newword+=morse[idx]
            if newword not in newlst:
                newlst.append(newword)
        return len(newlst)
      
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        s = "abcdefghijklmnopqrstuvwxyz"
        p = [".-","-...","-.-.","-..",".","..-.","--.","....",
             "..",".---","-.-",".-..","--","-.","---",".--.",
             "--.-",".-.","...","-","..-","...-",".--","-..-",
             "-.--","--.."]
        hashMap = {i:j for i,j in zip(s,p)}
        array = []
        for word in words:
            encoded_word = ""
            for w in word:
                 encoded_word += hashMap[w]
            if encoded_word not in array:
                array.append(encoded_word)
        return len(array)
