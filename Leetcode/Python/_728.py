class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        array = []
        for num in range(left, right+1):
            temp = num
            flag = True
            while temp > 0:
                r = temp % 10
                if r != 0 and num%r == 0:
                    temp //= 10
                else:
                    flag = False
                    temp = 0
                    break
            if flag:
                array.append(num)
        return array
