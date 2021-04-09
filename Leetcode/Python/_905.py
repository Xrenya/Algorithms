class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        index = 0
        
        while index < len(A):
            num = A[index]
            
            if num % 2 == 0:
                even_num = A.pop(index)
                A.insert(0, even_num)
            
            index += 1
        return A
      
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        array_even = []
        array_odd = []
        for num in A:
            if num % 2 == 0:
                array_even.append(num)
            else:
                array_odd.append(num)
        return array_even + array_odd

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        array = []
        for num in A:
            if num % 2 == 0:
                array = [num] + array
            else:
                array.append(num)
        return array
