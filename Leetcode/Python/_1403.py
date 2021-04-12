class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        def sortInplace(array):
            for j in range(1, len(array)):
                key = array[j]
                i = j - 1
                while i>-1 and key<array[i]:
                    array[i+1] = array[i]
                    i -= 1
                array[i+1] = key
            return array
        
        nums = sortInplace(nums)
        print(nums)
        acc = 0
        for num in nums:
            acc += num
        greater = 0
        array = []
        while greater<acc+1:
            num = nums.pop()
            array.append(num)
            greater += num
            acc -= num
        return array
