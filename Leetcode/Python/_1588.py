class Solution:
    # Brute force
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        acc = 0
        length = len(arr)
        for i in range(1,length+1,2):
            for j in range(length - i + 1):
                for digit in arr[0+j:i+j]:
                    acc += digit
        return acc

class Solution:
    # Brute force
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        acc = 0
        length = len(arr)
        for i in range(1,length+1,2):
            for j in range(length - i + 1):
                acc += sum(arr[0+j:i+j])
        return acc

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        acc = 0
        length = len(arr)
        for i in range(length):
            for j in range(i, length, 2):
                acc += sum(arr[i:j+1])
        return acc
