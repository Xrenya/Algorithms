class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = [(x[0], len(list(x[1]))) for x in groupby(sorted(nums))]
        sorted_new_array = sorted(counter, key=lambda x: (x[1], -x[0]))
        nums = []
        for i in sorted_new_array:
            nums += ([i[0]] * i[1])
        return nums
      
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        array = sorted(nums,key=nums.count)
        return array
