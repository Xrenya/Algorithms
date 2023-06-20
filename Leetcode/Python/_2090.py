class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        
        n = len(nums)
        averages = [-1] * n

        if 2 * k + 1 > n:
            return averages
        
        prefix = [0] * (n + 1)
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i - 1] + nums[i - 1]

        for i in range(k, n - k):
            left, right = i - k, i + k
            acc = prefix[right + 1] - prefix[left]
            avg = acc // (2 * k + 1)
            averages[i] = avg

        return averages
