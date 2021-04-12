class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashMap = {}
        for num in arr:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        array = hashMap.values()
        unique = {}
        for num in array:
            if num not in unique:
                unique[num] = 1
            else:
                return False
        return True

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashMap = {}
        for num in arr:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        unique = {}
        for num in hashMap.values():
            if num not in unique:
                unique[num] = 1
            else:
                return False
        return True
      
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashMap = {}
        for num in arr:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        return len(hashMap) == len(set(hashMap.values()))
    
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashMap = {}
        for num in arr:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        array = []
        for val in hashMap.values():
            array.append(val)
        return len(array) == len(set(array))
    
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashMap = {}
        for num in arr:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        array = []
        for val in hashMap.values():
            array.append(val)
        while array:
            num = array.pop()
            if num in array:
                return False
        return True
