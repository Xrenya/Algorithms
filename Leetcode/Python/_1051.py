import copy
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        def sortInplace(array):
            for j in range(1, len(array)):
                key = array[j]
                i = j - 1
                while i>-1 and array[i]>key:
                    array[i+1] = array[i]
                    i -= 1
                array[i+1] = key
            return array
        arr = copy.copy(heights)
        sortedHeight = sortInplace(arr)
        acc = 0
        for i in range(len(heights)):
            if sortedHeight[i] != heights[i]:
                acc += 1
        return acc
      
import copy
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        arr = copy.copy(heights)
        sortedHeight = sorted(arr)
        acc = 0
        for i in range(len(heights)):
            if sortedHeight[i] != heights[i]:
                acc += 1
        return acc
