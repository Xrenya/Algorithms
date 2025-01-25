class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_nums = sorted(nums)

        cur_group = 0
        num2groups = {}
        num2groups[sorted_nums[0]] = cur_group

        group2list = {}
        group2list[cur_group] = deque([sorted_nums[0]])

        for i in range(1, len(nums)):
            if abs(sorted_nums[i] - sorted_nums[i - 1]) > limit:
                cur_group += 1

            num2groups[sorted_nums[i]] = cur_group

            if cur_group not in group2list:
                group2list[cur_group] = deque()
            group2list[cur_group].append(sorted_nums[i])

        for i in range(len(nums)):
            num = nums[i]
            group = num2groups[num]
            nums[i] = group2list[group].popleft()

        return nums
