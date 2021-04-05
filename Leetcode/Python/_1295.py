class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            even_counter = 0
            while num != 0:
                num //= 10
                even_counter += 1   
            if even_counter%2 == 0:
                count += 1
        return count
      
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count
