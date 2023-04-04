class Solution:
    def partitionString(self, s: str) -> int:
        seen = [-1] * 26
        count = 1
        substring = 0
        
        for i in range(len(s)):
            if seen[ord(s[i]) - ord("a")] >= substring:
                count += 1
                substring = i
            seen[ord(s[i]) - ord("a")] = i
            
        return count
