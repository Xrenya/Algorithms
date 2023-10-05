class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mapping = {}
        output = []
        threshold = len(nums) // 3
        for n in nums:
            if n not in mapping:
                mapping[n] = 0
            mapping[n] += 1
        for k, v in mapping.items():
            if v > threshold:
                output.append(k)
        return output
        
