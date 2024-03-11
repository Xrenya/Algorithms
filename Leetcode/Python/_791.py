class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = defaultdict(int)
        
        for c in s:
            freq[c] += 1
            
        output = []
        for c in order:
            
            while freq[c]:
                output.append(c)
                freq[c] -= 1
                    
        for k, v in freq.items():
            if v > 0:
                output += k * v
                
        return "".join(output)
