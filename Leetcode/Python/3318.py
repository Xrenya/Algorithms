class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        output = []
        for i in range(n - k + 1):
            count = Counter(nums[i:i + k])
            freq = sorted(count.items(), key=lambda item: (-item[1], -item[0]))
            xsum = sum(key * value for key, value in freq[:x])
            output.append(xsum)
        return output
