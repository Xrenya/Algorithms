class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Time complexity O(n)
        # Space complexity O(n)
        hash = defaultdict(int)
        counter = 0
        for n in nums:
            if n in hash:
                counter += hash[n]
            hash[n] += 1
        return counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Time complexity O(n*(n-1))
        # Space complexity O(1)
        output = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    output += 1
        return output
