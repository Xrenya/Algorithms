class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        self.output = 0
        mapping = {}
        def backtrack(target):
            if target < 0:
                return 0
            
            if target == 0:
                return 1

            if target in mapping:
                return mapping[target]

            count = 0
            for n in nums:
                if target - n < 0:
                    break
                count += backtrack(target - n)
            mapping[target] = count
            return count

        return backtrack(target)
