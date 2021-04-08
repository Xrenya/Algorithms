class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string = ""
        lenght_1 = len(word1)
        lenght_2 = len(word2)
        if lenght_1 < lenght_2:
            lenght = lenght_1
        else:
            lenght = lenght_2
        for idx in range(lenght):
            string += word1[idx] + word2[idx]
        
        if lenght_1 < lenght_2:
            string += word2[lenght:]
        elif lenght_1 > lenght_2:
            string += word1[lenght:]
        return string
