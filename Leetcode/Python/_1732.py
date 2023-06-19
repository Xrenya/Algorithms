class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur_value = 0
        max_value = 0
        for n in gain:
            cur_value += n
            max_value = max(max_value, cur_value)
        return max_value
    
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        temp = 0
        for num in gain:
            temp += num
            if temp > highest:
                highest = temp
        return highest
