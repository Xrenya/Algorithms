class Solution:
    def maxDepth(self, s: str) -> int:
        maxDepth = 0
        depth = 0
        for string in s:
            if string is "(":
                depth += 1
            elif string is ")":
                depth -= 1
            if maxDepth < depth:
                maxDepth = depth
        return maxDepth
    
    
class Solution:
    def maxDepth(self, s: str) -> int:
        hashMap = {'(' : 1, ')' : -1}
        maxDepth = 0
        depth = 0
        for string in s:
            depth += hashMap.get(string, 0)
            if depth > maxDepth:
                maxDepth = depth
        return maxDepth
    
    
class Solution:
    def maxDepth(self, s: str) -> int:
        hashMap = {'(' : 1, ')' : -1}
        maxDepth = 0
        depth = 0
        for string in s:
            if string is "(" or string is ")":
                depth += hashMap[string]
                if depth > maxDepth:
                    maxDepth = depth
        return maxDepth
