class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        array = []
        for freq, val in zip(nums[0::2], nums[1::2]):
            array += [val] * freq
        return array
      
 class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        array = []
        for i in range(0,len(nums)-1,2): 
            array += nums[i]*[nums[i+1]]
        return array
