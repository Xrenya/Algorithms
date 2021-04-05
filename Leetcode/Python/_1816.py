class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        strArray = s.split(" ")
        return " ".join(strArray[:k])
            
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        strArray = s.split(" ")
        out_str = []
        for idx in range(k):
            out_str.append(strArray[idx])
        return " ".join(out_str)
