class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        def sortInplace(array):
            for j in range(1, len(array)):
                key = array[j]
                i = j - 1
                while i>-1 and key>array[i]:
                    array[i+1] = array[i]
                    i -= 1
                array[i+1] = key
            return array
        if len(target) < 2:
            return target == arr
        target = sortInplace(target)
        arr = sortInplace(arr)
        return target == arr
      
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target) < 2:
            return target == arr
        target = sorted(target)
        arr = sorted(arr)
        return target == arr
