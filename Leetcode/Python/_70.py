class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        first, second = 1, 2
        for i in range(3, n + 1):
            first, second = second, first + second
        return second
        

class Solution:
    def climbStairs(self, n: int) -> int:
        array = [0] * n
        if n == 1:
            return 1
        elif n == 2:
            return 2
        array[0] = 1
        array[1] = 2
        for i in range(2, n):
            array[i] = array[i - 1] + array[i - 2]
        return array[-1] 


class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 2
        if n == 1:
            return first
        elif n == 2:
            return second
        for i in range(3, n + 1):
            first, second = second, first + second, 
        return second


class Solution:
    # Faster
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        n1 = 1
        n2 = 2
        for i in range(2, n):
            temp = n2
            n2 = n1 + n2
            n1 = temp
        return n2


class Solution:
    # Less memory
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        array = [0] * n
        array[0] = 1
        array[1] = 2
        for i in range(2, n):
            array[i] += array[i - 1]
            array[i] += array[i - 2]
        return array[n - 1]
            
