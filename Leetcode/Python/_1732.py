class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        temp = 0
        for num in gain:
            temp += num
            if temp > highest:
                highest = temp
        return highest
