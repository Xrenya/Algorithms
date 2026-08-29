class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_nums = sorted(nums)

        group = 0
        group2num = {group: deque([sorted_nums[0]])}
        num2group = {sorted_nums[0]: group}

        for i in range(1, len(nums)):
            if sorted_nums[i] - sorted_nums[i - 1] > limit:
                group += 1
            if group not in group2num:
                group2num[group] = deque([])
            
            group2num[group].append(sorted_nums[i])

            if sorted_nums[i] not in num2group:
                num2group[sorted_nums[i]] = group

        for i in range(len(nums)):
            num = nums[i]
            group = num2group[num]
            nums[i] = group2num[group].popleft()
            
        return nums

