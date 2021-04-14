from copy import copy 
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        rows = len(strs)
        cols = len(strs[0])
        for col in range(cols):
            stringArray = []
            for row in range(rows):
                stringArray.append(strs[row][col])
            array = stringArray.copy()
            array = sorted(array)
            if stringArray != array:
                count += 1
        return count
      
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        rows = len(strs)
        cols = len(strs[0])
        for col in range(cols):
            for row in range(rows-1):
                if strs[row][col] > strs[row+1][col]:
                    count += 1
                    break      
        return count
