class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        unique = []
        for n in nums:
            if unique and unique[-1] != n:
                unique.append(n)
            elif not unique:
                unique.append(n)
        counter = 0
        for i in range(1, len(unique) - 1):
            if (unique[i - 1] < unique[i] and unique[i] > unique[i + 1]) or (unique[i - 1] > unique[i] and unique[i] < unique[i + 1]):
                counter += 1
        return counter
