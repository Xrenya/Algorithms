class Solution:
    def maximum69Number (self, num: int) -> int:
        hashMap = {0:0, 1:3, 2:30, 3:300, 4:3000}
        number = num
        count = 1
        idx = 0
        while number != 0:
            if number % 10 == 6:
                idx = count
            number //= 10
            count += 1
        return num + hashMap[idx]
      
class Solution:
    def maximum69Number (self, num: int) -> int:
        number = num
        count = 1
        idx = -1
        while number != 0:
            if number % 10 == 6:
                idx = count
            number //= 10
            count += 1
        return num + 3*(10**(idx-1)) if idx != -1 else num
