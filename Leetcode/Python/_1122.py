class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hashMap = collections.Counter(arr1)
        array = []
        for num in arr2:
            array += [num] * hashMap.pop(num)
            
        return array + sorted(hashMap.elements())
    
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hashMap = collections.Counter(arr1)
        array = []
        for num in arr2:
            array += [num] * hashMap.pop(num)
            
        for num in sorted(hashMap.keys()):
            array += [num] * hashMap[num]
            
        return array

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hashMap = {}
        for num in arr1:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        array = []
        for num in arr2:
            array += [num] * hashMap.pop(num)
            
        for num in sorted(hashMap.keys()):
            array += [num] * hashMap[num]
            
        return array
