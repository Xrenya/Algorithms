class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        hashMap = {}
        max_value = 0
        for box_id in range(lowLimit, highLimit+1):
            runner = box_id
            box_num = 0
            while runner > 0:
                box_num += (runner%10)
                runner //= 10
            if box_num not in hashMap:
                hashMap[box_num] = 1
            else:
                hashMap[box_num] += 1
            if hashMap[box_num] > max_value:
                max_value = hashMap[box_num]
        return max_value
      
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        hashMap = {}
        max_value = 0
        for box_id in range(lowLimit, highLimit+1):
            runner = box_id
            box_num = 0
            while runner > 0:
                box_num += (runner%10)
                runner //= 10
            if box_num not in hashMap:
                hashMap[box_num] = 1
            else:
                hashMap[box_num] += 1
        array = hashMap.values()
        return max(array)
