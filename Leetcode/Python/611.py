class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # def check_sides(a, b, c):
        #     if (a + b) > c and (b + c) > a and (a + c) > b:
        #         return True
        #     return False

        # def recursive(index, tmp):
        #     if len(tmp) == 3:
        #         if check_sides(*tmp):
        #             self.output += 1
        #             return

        #     for i in range(index, len(nums)):
        #         tmp.append(nums[i])
        #         recursive(i + 1, tmp)
        #         tmp.pop()

        # self.output = 0
        # recursive(0, [])
        # return self.output
        # TLE solution

        output = 0
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                continue
            k = i + 2
            for j in range(i + 1, len(nums) - 1):
                while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    k += 1
                output += k - j - 1

        return output
