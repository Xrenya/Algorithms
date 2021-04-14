class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        dif = arr[1] - arr[0]
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] != dif:
                return False
        return True
      
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        def sortInplace(array):
            for j in range(1, len(array)):
                key = array[j]
                i = j - 1
                while i > -1 and key>array[i]:
                    array[i+1] = array[i]
                    i -= 1
                array[i+1] = key
            return array
        arr = sortInplace(arr)
        dif = arr[1] - arr[0]
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] != dif:
                return False
        return True
        
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        dif = arr[1] - arr[0]
        array = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
        return len(set(array)) == 1
      
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        i = arr[:len(arr)-1]
        j = arr[1:]
        array = [i - j for i, j in zip(i, j)]
        return len(set(array)) == 1
        
