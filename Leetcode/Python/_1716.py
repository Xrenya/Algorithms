class Solution:
    def totalMoney(self, n: int) -> int:
        acc = 0
        whole = n // 7
        mod = n % 7
        for i in range(whole):
            acc += 28 + 7*i
        if whole == 0:
            i = 0
            for j in range(mod):
                i += 1
                acc += i
        else:
            for j in range(mod):
                i += 1
                acc += i+1
        return acc
                
                
        
