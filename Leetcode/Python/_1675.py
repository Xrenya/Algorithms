class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = -((nums[i] << 1) if nums[i] & 1 == 1 else nums[i])

        min_num = -max(nums)
        max_nums = nums
        heapq.heapify(max_nums)

        min_deviation = math.inf
        while True:
            max_num = -max_nums[0]
            deviation = max_num - min_num

            if deviation < min_deviation:
                min_deviation = deviation
                if min_deviation == 0:
                    break

            if max_num & 1 == 1:
                break

            max_num >>= 1
            heapq.heapreplace(max_nums, -max_num)
            if max_num < min_num:
                min_num = max_num

        return min_deviation
      
# The input array is modified to turn every odd number negative and double its value. This is done by iterating over every element of the input array, checking if it's odd or even, and applying the appropriate operation using bitwise operators. This is done so that we can perform only the "divide by 2" operation in the following steps, which simplifies the problem.
# The maximum number in the modified array is assigned to a variable named "minNum". This is because we want to minimize the deviation of the array, and having a larger minimum number in the array would increase the deviation.
# A heap is created from the modified array. The heap is used to keep track of the maximum value in the array, which we can modify by dividing it by 2.
# A variable named "minDeviation" is initialized to infinity. This variable will be used to keep track of the minimum deviation we have encountered so far.
# We enter a while loop that will terminate only when we have found the minimum deviation or when we can no longer perform any operations.
# The maximum value in the heap is extracted and assigned to a variable named "maxNum".
# The deviation of the array is calculated as the difference between the maximum value (after dividing by 2 if it's even) and the minimum value.
# If the deviation is less than the minimum deviation seen so far, it is updated as the new minimum deviation.
# If the maximum value is odd, we can no longer perform any operations and we break out of the while loop.
# If the maximum value is even, we divide it by 2 and replace the maximum value in the heap with the new value.
# If the new maximum value is less than the current minimum value, we update the minimum value to be the new maximum value.
# The loop continues until we have found the minimum deviation or can no longer perform any operations.
# The minimum deviation is returned as the final result.
