class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        hashMap = {}
        for num in A:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                return num
              
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        array = []
        for num in A:
            if num not in array:
                array.append(num)
            else:
                return num
