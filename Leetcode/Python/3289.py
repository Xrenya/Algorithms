class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        output = []
        mapping = set()
        for n in nums:
            if n in mapping:
                output.append(n)
            mapping.add(n)
        return output
