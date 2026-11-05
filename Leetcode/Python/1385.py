class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        output = 0
        for i in range(len(arr1)):
            if all(abs(arr1[i] - y) > d for y in arr2):
                output += 1

        return output
