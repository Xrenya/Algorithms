class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        count = [0] * n
        occurance = [0] * n
        cur = 0
        for i in range(n):
            occurance[A[i] - 1] += 1
            occurance[B[i] - 1] += 1

            if occurance[A[i] - 1] == 2:
                cur += 1
            if B[i] != A[i] and occurance[B[i] - 1] == 2:
                cur += 1
            count[i] = cur
        return count
