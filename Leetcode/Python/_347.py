class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}
        for num in nums:
            if num not in mapping:
                mapping[num] = 0
            mapping[num] += 1
        output = []
        for k, val in sorted(mapping.items(), key=lambda item: item[1], reverse=True)[:k]:
            output.append(k)
        return output
    
    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
        lst = sorted(counter.items(), key=lambda item: item[1])[-k:]
        out = [(lambda x: x[0])(x) for x in lst]
        
        return out
