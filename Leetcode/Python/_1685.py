class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        n = len(nums)
        left_sum = 0

        output = []
        for i in range(n):
            right_sum = total - left_sum - nums[i]

            left_count = i
            right_count = n - 1 - i

            left_total = left_count * nums[i] - left_sum
            right_total = right_sum - right_count * nums[i]

            output.append(left_total + right_total)
            left_sum += nums[i]
        return output


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        suffix = [0] * n
        suffix[-1] = nums[-1]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        output = []
        for i in range(n):
            left_sum = prefix[i] - nums[i]
            right_sum = prefix[-1] - prefix[i]

            left_count = i
            right_count = n - 1 - i

            left_total = left_count * nums[i] - left_sum
            right_total = right_sum - right_count * nums[i]

            output.append(left_total + right_total)
        return output


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        suffix = [0] * n
        suffix[-1] = nums[-1]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i]


        output = []
        for i in range(n):
            if i == 0:
                output.append(suffix[i + 1] - nums[i] * (n - 1))
            elif i == n - 1:
                output.append(nums[i] * (n - 1) - prefix[i - 1])
            else:
                output.append(nums[i] * i - prefix[i - 1] + suffix[i + 1] - nums[i] * (n - i - 1))
        return output
