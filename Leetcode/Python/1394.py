class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashMap = {}
        for i in arr:
            hashMap[i] = hashMap.get(i, 0) + 1
        return max([key for key, value in hashMap.items() if key == value], default=-1)
      
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashMap = Counter(arr)
        output = -1
        for key, val in hashMap.items():
            if key == val:
                if output < val:
                    output = val
        return output
      
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashMap = {}
        for num in arr:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        output = -1
        for key, val in hashMap.items():
            if key == val:
                if output < val:
                    output = val
        return output
