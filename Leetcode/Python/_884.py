class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        hashMap  = {}
        words = B.split(" ") + A.split(" ")
        
        for word in words:
            if word not in hashMap:
                hashMap[word] = 1
            else:
                hashMap[word] += 1
        output = []        
        for key, val in hashMap.items():
            if val == 1:
                output.append(key)
        return output
