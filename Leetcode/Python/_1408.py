class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output = []
        words = sorted(words, key=lambda x: len(x), reverse=True)
        flag = True
        while flag:
            if len(words)==0:
                flag=False
                break
            word = words.pop()
            for token in words:
                if len(word) > len(token):
                    flag=False
                    break
                elif word in token and word not in output:
                    output.append(word)
        return output
                    
