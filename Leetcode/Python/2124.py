class Solution:
    def checkString(self, s: str) -> bool:
        found = False
        foundB = False
        for char in s:
            if char == 'a':
                if foundB:
                    return False
                found = True
            elif char == 'b':
                foundB = True
        
        return found or foundB
