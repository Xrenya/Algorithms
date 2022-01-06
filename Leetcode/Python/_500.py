class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        FIRST = "qwertyuiop"
        SECOND = "asdfghjkl"
        THIRD = "zxcvbnm"
        output = []
        for word in words:
            for L in [FIRST, SECOND, THIRD]:
                flag = True
                for c in word:
                    # print(c.lower(), L, c.lower() not in L)
                    if c.lower() not in L:
                        flag = False
                        break
                if flag:
                    output.append(word)
        return output
